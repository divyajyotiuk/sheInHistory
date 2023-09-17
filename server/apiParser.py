from apiWrapper import apiWrap
from googlesearch import search
import openai
from decouple import config
import json
from db import Database
from webCrawler import process_state_data

from flask import Flask

app = Flask(__name__)


# Access the secret key from the .env file
secret_key = config('SECRET_KEY')

# Use the secret_key in your code
# print(f"My secret key is: {secret_key}")

class apiParser:
        

    def videoUrls(state_name):
        # Define the search query with the state name
        
        search_query = f"Historical data {state_name} site:youtube.com"

        # Number of search results to retrieve
        num_results = 10

        # Fetch search results and filter for URLs from the "Videos" section
        video_urls = []

        for url in search(search_query, num_results=num_results):
            if "youtube.com" in url:
                video_urls.append(url)

        # Print URLs from the "Videos" section
        for url in video_urls:
            print(f"Video URL: {url}")
        return video_urls
    
    def returnUrl(state_name):
        
        search_query = f"Women Historical data {state_name}"

        # Number of search results to retrieve
        num_results = 10

        # Fetch search results and print URLs
        search_results = search(search_query, num_results=num_results)
        for url in search_results:
            print(f"URL: {url}")
        return search_results
    
    def createAPI(state_name,data):
        paragraphs=data
        prompt = f"""REQUIREMENTS:

        Give only json response with below requirements:
        - each object should contain 3 keys: dates, events, persons 
        - dates is an array of objects with keys year and title from below data
        - events is an array of objects with keys head and desc from below data
        - persons is an array of objects with keys name and wikipedia link of the person from below data
        {paragraphs}
        
        """
        openai.api_key =secret_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

    # Parse the JSON response to get an array of objects
        json_API = json.loads(response.choices[0].message.content)
        # print(json_API)
        return json_API
    
# main function to get jsonAPI
def main(state_name):
    db = Database(app)
    
    videourls=apiParser.videoUrls(state_name)
    urls=apiParser.returnUrl(state_name)
    data=process_state_data(state_name)
    # data=data.split()[:4097]
    # data=" ".join(data)
    # print("********************",data)
    obj=apiWrap(urls,videourls,state_name,data,{})
    #
    data=data.split()[:1000]
    data=" ".join(data)
    # print("data",data)
    jsonAPI=apiParser.createAPI(state_name,data)
    print("jsonAPI",jsonAPI)
    jsonAPI['state']=state_name
    jsonAPI["video_urls"] = videourls
    jsonAPI["website_urls"] = urls
    # updated_json = json.dumps(jsonAPI, indent=4)
    # obj.jsonAPI=updated_json
    print("jsonAPI33333333333333333333333333333333333%",jsonAPI)

    db.addEntry(jsonAPI)
    # print(updated_json)
main("Florida")


        

    





        
    

    
    

    



