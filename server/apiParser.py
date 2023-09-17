from apiWrapper import apiWrap
from googlesearch import search
import openai
from decouple import config
import json

# Access the secret key from the .env file
secret_key = config('SECRET_KEY')

# Use the secret_key in your code
# print(f"My secret key is: {secret_key}")

class apiParser:

    def videoUrls(self,state_name):
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
    
    def returnUrl(self,state_name):
        
        search_query = f"Women Historical data {state_name}"

        # Number of search results to retrieve
        num_results = 10

        # Fetch search results and print URLs
        search_results = search(self,search_query, num_results=num_results)
        for url in search_results:
            print(f"URL: {url}")
        return search_results
    
    def createAPI(self,state_name,data):
        paragraphs=data
        prompt = f"""REQUIREMENTS:

        Give only json response with below requirements:
        - Identify different women and write details about each in json format
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
        json_API = response.choices[0].message.content
        print(json_API)
        return json_API
    
# main function to get jsonAPI
    def main(self,state_name):
        
        videourls=self.videoUrls(state_name)
        urls=self.returnUrl(state_name)
        data=[]

        obj=apiWrap(urls,videourls,state_name,data,{})
        jsonAPI=self.createAPI(state_name,data)
        jsonAPI["state"]=state_name
        jsonAPI["video_urls"] = videourls
        jsonAPI["website_urls"] = urls
        updated_json = json.dumps(jsonAPI, indent=4)
        obj.jsonAPI=updated_json
        print(updated_json)


        

    





        
    

    
    

    



