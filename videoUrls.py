from googlesearch import search

# Define the search query with the state name
state_name = "New York"
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
    