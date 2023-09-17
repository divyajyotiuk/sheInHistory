def urls(state_name):
    search_query = f"Women Historical data {state_name}"

    # Number of search results to retrieve
    num_results = 10
    ans=[]
    # Fetch search results and print URLs
    search_results = search(search_query, num_results=num_results)
    print(search_results)
    for url in search_results:
        ans.append(url)
    print(ans)
    return(ans)
def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content_div = soup.find("div", class_="mw-parser-output")

    historical_info = ""

    for paragraph in content_div.find_all("p"):
        historical_info += paragraph.get_text() + "\n"

    
        return historical_info

urlsResult=urls("Florida")
result=[]
for i in urlsResult:
    ans=scrape(i)
    result.append(ans)
  