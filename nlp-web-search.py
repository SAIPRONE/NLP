# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:20:55 2023

@author: Fadi Helal
"""
#%% Tokenizing the User's Query
import nltk 
from nltk.tokenize import word_tokenize

# Download the punkt tokenizer
nltk.download('punkt')

def tokenize_query(query):
    return word_tokenize(query)

#%% Making a Request to the Search Engine
import requests 
import json
from bs4 import BeautifulSoup

def google_search (query, api_key, cx):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'key': api_key,
        'cx':cx
        }
 
    response = requests.get(base_url, params=params)

    return response.json()
#%% Parsing the Search Results
def parse_results(soup):
    # Find all div elements with class name BNeawe
    result_divs = soup.find_all('div', class_='BNeawe')
    results = [div.get_text() for div in result_divs]
    return results

#%% Putting It All Together
def main():
    cx = "your CX" # your programable serach engine ID
    api_key = "your API KEY"
    
    while True:
        user_query = input("\nEnter your query (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break

        results = google_search(user_query, api_key, cx)
        if 'items' in results:
            print("\nSearch results: ")
            for result in results['items']:
                print(result['title'])
                print(result['link'])
                print(result['snippet'])
                print("\n")
        else:
            print("\nNo results found.\n")
    
    print("Thank you for using the search tool.")

if __name__ =="__main__":
    main()     