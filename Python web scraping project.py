# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 08:19:51 2024

@author: koox5
"""

import requests
from bs4 import BeautifulSoup

# URL of the website
url = "http://quotes.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all quotes on the page
    quotes = soup.find_all('span', class_='text')

    # Print each quote
    for quote in quotes:
        print(quote.text)
else:
    print("Failed to retrieve the page")

import pandas as pd 

quotes_data = []

for quote in quotes:
    # Try to find the author
    author = quote.find_previous('small', class_='author')
    
    # If author is found, get the text; otherwise, use a placeholder
    author_name = author.text if author else 'Unknown Author'

    # Similarly, extract tags, using a fallback if no tags are found
    tags = ', '.join([tag.text for tag in quote.find_all_next('a', class_='tag')])

    quotes_data.append({
        "quote": quote.text,
        "author": author_name,
        "tags": tags
    })

# Create a DataFrame
df = pd.DataFrame(quotes_data)

# Save the DataFrame to a CSV file
df.to_csv('quotes.csv', index=False)

print("Data saved to quotes.csv")

