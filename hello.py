import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://appwrite.io/'

# Send a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find specific elements on the webpage using BeautifulSoup's methods
    # For example, let's extract all the <h2> tags from the webpage
    elements_with_hello_class = soup.find_all(class_='web-main-header is-special-padding theme-dark is-transparent svelte-go26dj')
    
    # Print the text content of each <h2> tag
    for i in elements_with_hello_class:
        print(i.text)
else:
    print('Failed to retrieve webpage. Status code:', response.status_code)