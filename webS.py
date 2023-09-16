import openai
import requests
from bs4 import BeautifulSoup
from googlesearch import search  # Import the search function

# Set your OpenAI API key
api_key = "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"

# Function to process and represent historical data using OpenAI GPT-3
def process_and_represent_data(data):
    try:
        # Initialize the OpenAI API client
        openai.api_key = api_key

        # Define the prompt for GPT-3
        prompt = f"Summarize the following historical data and keep information related to women history in new york:\n{data}\n\n"

        # Request a completion from GPT-3
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,  # Adjust the max tokens as needed
            n=1,  # Number of responses to generate
            stop=None,  # You can specify a stop sequence if needed
            temperature=0.7  # Adjust the temperature for creativity
        )

        # Get the generated text from the response
        generated_text = response.choices[0].text.strip()

        return generated_text

    except Exception as e:
        print(f"Error while processing data: {str(e)}")
        return None

# Function to scrape and process historical data from a given URL
def scrape_and_process_url(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract historical data (modify this based on the actual webpage structure)
            historical_data = ""
            # Example: historical_data = soup.find('div', class_='historical-data').get_text()

            # Process the historical data using OpenAI
            generated_representation = process_and_represent_data(historical_data)

            return generated_representation

        else:
            print(f"Failed to retrieve data from URL: {url}")
            return None

    except Exception as e:
        print(f"Error while scraping and processing URL: {str(e)}")
        return None

# Function to perform a Google search and get a list of URLs
def perform_google_search(query, num_results=10):
    try:
        search_results = list(search(query))
        return search_results

    except Exception as e:
        print(f"Error while performing Google search: {str(e)}")
        return []

# Define your Google search query
google_query = "Women's history in New York"

# Perform the Google search and get a list of URLs
search_results = perform_google_search(google_query)

# Dictionary to store results
result = {}

# Loop through each URL from the search results, scrape and process data, and add it to the result
for url in search_results:
    generated_representation = scrape_and_process_url(url)
    if generated_representation:
        result[url] = generated_representation

# Print the result
for url, representation in result.items():
    print(f"URL: {url}")
    print(f"Generated Representation:\n{representation}\n")
