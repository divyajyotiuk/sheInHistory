
from googlesearch import search
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import spacy

# def clean(text):
  
#     nlp = spacy.load("en_core_web_sm")

#     doc = nlp(text)

#     min_sentence_length = 4  
#     max_sentence_length = 20  


#     filtered_sentences = [
#         sent.text for sent in doc.sents
#         if min_sentence_length <= len(sent) <= max_sentence_length
#     ]

#     # Combine the filtered sentences into a single string
#     ans = " ".join(filtered_sentences)
#     return ans

# ##url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
# def returndata(url):
#   html = urlopen(url).read()
#   soup = BeautifulSoup(html, features="html.parser")

#   # kill all script and style elements
#   for script in soup(["script", "style"]):
#       script.extract()    # rip it out

#   # get text
#   text = soup.get_text()

#   # break into lines and remove leading and trailing space on each
#   lines = (line.strip() for line in text.splitlines())
#   for line in lines:
#         line = clean(line)
#         if len(line) > 2:
#             continue
#         else:
#            lines.remove(line)

#   # break multi-headlines into a line each
#   chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
#   # drop blank lines
#   chunks = clean(" ".join(chunks)) 
#   chunks=chunks[200:-200]

#   print("hererere",text)

def urls(state_name):
    search_query = f"Women Historical data {state_name}"

    # Number of search results to retrieve
    num_results = 10
    ans=[]
    # Fetch search results and print URLs
    search_results = search(search_query)
    print(search_results)
    for url in search_results:
        ans.append(url)
    print(ans)
    return(ans)

state="Florida"
urlsResult=urls(state)
result=""
count=0




def clean(text):
  
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)

    min_sentence_length = 4  
    max_sentence_length = 60 


    filtered_sentences = [
        sent.text for sent in doc.sents
        if min_sentence_length <= len(sent) <= max_sentence_length
    ]

    # Combine the filtered sentences into a single string
    ans = " ".join(filtered_sentences)
    return ans

def returndata(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    for line in lines:
        line = clean(line)
        if len(line) > 2:
            print(line)

    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    chunks = clean(" ".join(chunks))  # Clean and join the chunks

    # drop blank lines
    print(chunks[200:-200])

for i in urlsResult:


  try:
    ans=returndata(i)
    result+=ans
    count+=1
    if(count==4):
      break
  except Exception as e:
    pass
print("&&&&&&&&",result)
