import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://pizzaboccalupo.com'

# Send a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find specific elements on the webpage using BeautifulSoup's methods
    # For example, let's extract all the <h1> tags from the webpage
    headings = soup.find_all('h2')
    
    # Print the text content of each <h1> tag
    for heading in headings:
        print(heading.text)
else:
    print('Failed to retrieve webpage. Status code:', response.status_code)