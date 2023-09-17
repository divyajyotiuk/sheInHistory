import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/History_of_New_York_(state)"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main content div
content_div = soup.find("div", class_="mw-parser-output")

# Initialize a variable to store the historical information
historical_info = ""

# Loop through the paragraphs within the content div
for paragraph in content_div.find_all("p"):
    # Append the text of each paragraph to the historical_info variable
    historical_info += paragraph.get_text() + "\n"

# Print or use the historical_info as needed
print(historical_info)
