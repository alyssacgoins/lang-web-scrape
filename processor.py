from cleaner import process_word
from retriever import scrape_body_text
import concurrent.futures
import pandas as pd
import csv

""" Call processing functions """
def process(url):
  process_body_text(scrape_body_text(url))


""" Execute concurrent cleaning for input body_text_entries and write data to
    csv file. """
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
        write_body_text_to_csv(future, 'body-text.csv')
      except Exception as exc:
        print(f"Source generated an exception")


""" Write input csv list to input csv file name.  """
def write_body_text_to_csv(csv_list, csv_file_name):
  # return data by retrieving the tag content
  with open(csv_file_name, 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_list)

""" Return input dataframe split into chunk_size-sized lists."""
def split_data(dataframe, chunk_size):
  list = dataframe.values.flatten().tolist()
  return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]


""" Return input csv list with each entry of input dataframe processed."""
def row_iterator(dataframe, csv_list):
  for item in dataframe:
    process_word(item, csv_list)
  return csv_list


""" Return row_iterator() method call for input dataframe and empty string 
    list."""
def worker(dataframe):
  return row_iterator(dataframe, [''])
