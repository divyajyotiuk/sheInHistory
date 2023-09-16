from googlesearch import search

# Define the search query with the state name
state_name = "New York"
def urls(state_name):
  search_query = f"Women Historical data {state_name}"

  # Number of search results to retrieve
  num_results = 10

  # Fetch search results and print URLs
  search_results = search(search_query, num_results=num_results)
  for url in search_results:
      print(f"URL: {url}")
urls(state_name)