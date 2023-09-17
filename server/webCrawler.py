from googlesearch import search
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import spacy
import re
def clean(text):
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)
    # print(doc)
    min_sentence_length = 60
    max_sentence_length =  100
    filtered_sentences=[]
    for sent in doc.sents:
        cleaned_text = re.sub(r'\s+', ' ', sent.text).strip()

        if len(cleaned_text)>60:
            filtered_sentences.append(cleaned_text)
        # print(sent.text)
    # filtered_sentences = [
    #     sent.text for sent in doc.sents
    #     if min_sentence_length <= len(sent) <= max_sentence_length
    # ]
    # print("******************************",filtered_sentences)
    # Combine the filtered sentences into a single string
    ans = " ".join(filtered_sentences)
    cleaned_text2 = ans.strip()

    # print(cleaned_text2)
    return ans

def returndata(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.body.get_text()
    # cleaned_text = re.sub(r'\s+', ' ', text).strip()
    # print("text^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",cleaned_text[30:])
    # break into lines and remove leading and trailing space on each
    lines =[]
    for line in text.splitlines():
        temp=line.strip()
        if len(temp)>0:
            if(len(temp.split())>6):
                lines.append(temp)
    # cleanedLines=[]
    # for line in lines:
    #     if line!="":
    #         line = clean(line)
    #         cleanedLines.append(line)
        # if len(line) > 2:
        #     print(line)

    # # break multi-headlines into a line each
    # chunks = (phrase.strip() for line in cleanedLines for phrase in line.split("  "))
    # chunks = clean(" ".join(chunks))  # Clean and join the chunks
    # print("chunk**********************************************",chunks)
    # # drop blank lines
    # # print(chunks[200:-200])
    # return chunks[200:-200]
    ans = " ".join(lines)
    return ans

def process_state_data(state_name):
    # Step 1: Search for URLs
    def urls(state_name):
        search_query = f"Women Historical data {state_name}"
        num_results = 10
        ans = []
        search_results = search(search_query)
        for url in search_results:
            ans.append(url)
        return ans

    urlsResult = urls(state_name)
    result = ""
    count = 0

    # Step 2: Extract and process data from URLs
    for i in urlsResult:
        try:
            ans = returndata(i)
            result += ans
            count += 1
            if count == 4:
                break
        except Exception as e:
            pass
    print("&&&&",result)
    return result

# process_state_data("Florida")