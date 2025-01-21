from bs4 import BeautifulSoup
import requests as req
from clean import process_word
import pandas as pd
import threading

""" Scrapes data from input webpage and saves body text to csv. """
def scrape_body_text(url):
  try:
    response = req.get(url)

    # create BeautifulSoup object with html parser
    soup = BeautifulSoup(response.text, "html.parser")
    # remove tags
    for data in soup(['style', 'script']):
      data.decompose()

    # create string list of body text entries
    body_text_entries = ['']
    for entry in soup.stripped_strings:
      for word in entry.split():
        body_text_entries.append(word)
    return body_text_entries
  except:
    print()

def handle_body_text(body_text_entries):
  # remove duplicate words via pandas DataFrame
  dataframe = pd.DataFrame(body_text_entries)
  dataframe = dataframe.drop_duplicates()

  csv_list = ['']
  for row in dataframe.iterrows():
    word = row[1][0]
    process_word(word, csv_list)
  return csv_list