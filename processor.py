from cleaner import process_word
from retriever import scrape_body_text
import concurrent.futures
import pandas as pd
import csv

""" Return  """
def process(url):
  list = process_body_text(scrape_body_text(url))
  #write_body_text_to_csv(list)

def write_body_text_to_csv(csv_list):
  # # return data by retrieving the tag content
  with open('body-text.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_list)

""" Return true if Executes API call to merriam-webster dictionary API to determine if 
    word is English. """
def process_body_text(body_text_entries):
  # remove duplicate words via pandas DataFrame
  dataframe = pd.DataFrame(body_text_entries)
  dataframe = dataframe.drop_duplicates()

  # split dataframe
  chunks = split_data(dataframe, 10)

  with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = list(executor.map(worker, chunks))

    for future in futures:

      try:
        write_body_text_to_csv(future)
        #print(f"Source {source}: {data}")
      except Exception as exc:
        print(f"Source generated an exception")

""" Return input dataframe split into chunk_size-sized lists."""
def split_data(dataframe, chunk_size):
  list = dataframe.values.flatten().tolist()
  return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]


def row_iterator(dataframe, csv_list):
  for item in dataframe:
    process_word(item, csv_list)
  return csv_list

def worker(dataframe):
  return row_iterator(dataframe, [''])
