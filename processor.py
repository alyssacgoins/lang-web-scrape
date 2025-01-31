from concurrent.futures.thread import ThreadPoolExecutor

import concurrent.futures
import pandas as pd
import csv

""" Orchestrate input Cleaner to process html web text. """
class Processor:

  """ Initialize processor instance. """
  def __init__(self, cleaner):
    self.cleaner = cleaner
    self.clear_file('body-text.csv')

  """ Execute concurrent cleaning on input body text and write data to csv. """
  # todo handle capitalized/non-capitalized duplicates.
  # todo run perf testing to optimize chunk/worker sizing
  def process_body_text(self, body_text_entries):
    # create dataframe from input list, remove duplicates & split into chunks
    dataframe = pd.DataFrame(body_text_entries).drop_duplicates()
    lists = self.split_dataframe_to_lists(dataframe, 100)

    # concurrently clean dataframe entries & write output to body-text.csv
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
      futures = list(executor.map(self.worker, lists))
      for future in futures:
        try:
          self.write_body_text_to_csv(future, 'body-text.csv')
        except Exception as exc:
          raise Exception(exc)

  """ Clear the contents of the file at input filename. """
  @staticmethod
  def clear_file(file_name):
    f = open(file_name, 'w')
    f.truncate()
    f.close()

  """ Return input dataframe split into input chunk_size-sized lists."""
  @staticmethod
  def split_dataframe_to_lists(dataframe, list_size):
    df_as_list = dataframe.values.flatten().tolist()
    return [df_as_list[i:i + list_size] for i in
            range(0, len(df_as_list), list_size)]

  """ Return clean_dataframe() method call on input dataframe. """
  def worker(self, input_list):
    return self.clean_list(input_list)

  """ Return csv list containing each entry of input dataframe, cleaned for 
      punctuation and target language. """
  def clean_list(self, input_list):
    csv_list = []

    for entry in input_list:
      word = self.cleaner.clean_word(entry)
      if word != '':
        csv_list.append(word)
    return csv_list

  """ Write input csv list to input csv file name.  """
  @staticmethod
  def write_body_text_to_csv(csv_list, csv_file_name):
    # return data by retrieving the tag content
    with open(csv_file_name, 'a') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(csv_list)