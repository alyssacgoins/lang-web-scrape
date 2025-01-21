from bs4 import BeautifulSoup
import requests as req
from clean import process_word
import pandas as pd
import concurrent.futures

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

  # split dataframe
  chunks = split_data(dataframe, 100)

  with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    results = list(executor.map(worker, chunks))

# Split the data into chunks
def split_data(df, chunk_size):
  list = df.values.flatten().tolist()
  return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]

def row_iterator(dataframe):
  csv_list = ['']
  for item in dataframe:
    process_word(item, csv_list)
  return csv_list

def worker(dataframe):
  row_iterator(dataframe)