from concurrent.futures.thread import ThreadPoolExecutor

import concurrent.futures
import pandas as pd
import csv

""" Utilize input Retriever and Cleaner to process web text. """
class Processor:

  """ Initialize processor instance. """
  def __init__(self, retriever, cleaner):
    self.cleaner = cleaner
    self.retriever = retriever
    self.clear_file('body-text.csv')

  # list containing German-language articles
  articles = ['der', 'die', 'das', 'den', 'dem', 'des', 'ein', 'eine',
              'einer', 'einem', 'einen']

  """ Execute web scraping and process the retrieved text. """
  def process(self):
    body_text = self.soup_to_list(self.retriever.scrape_body_text())
    # clear csv files
    self.process_body_text(body_text)

  """ Clear the contents of the file at input filename. """
  @staticmethod
  def clear_file(file_name):
    f = open(file_name, 'w')
    f.truncate()
    f.close()

  """ Return input BeautifulSoup text in list form. """
  def soup_to_list(self, soup):
    # create string list of body text entries
    body_text_entries = ['']
    for entry in soup.stripped_strings:

      word_follows_article = False
      for word in entry.split():
        # if word directly follows an article, skip word (already processed)
        if word_follows_article:
          word_follows_article = False
          continue
        # if word is article, retrieve following word & append pair to list
        elif self.is_article(word):
          substring = self.get_article_and_word(entry, word)
          body_text_entries.append(substring)
          word_follows_article = True
        # append word to list
        else:
          body_text_entries.append(word)
    return body_text_entries

  """ Execute concurrent cleaning on input body text and write data to csv. """
  # todo handle capitalized/non-capitalized duplicates.
  # todo run perf testing to optimize chunk/worker sizing
  def process_body_text(self, body_text_entries):
    # create dataframe from input list, remove duplicates & split into chunks
    dataframe = pd.DataFrame(body_text_entries).drop_duplicates()
    chunks = self.split_dataframe(dataframe, 100)

    # concurrently clean dataframe entries & write output to body-text.csv
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
      futures = list(executor.map(self.worker, chunks))
      for future in futures:
        try:
          self.write_body_text_to_csv(future, 'body-text.csv')
        except Exception as exc:
          raise Exception(exc)

  """ Return true if input word is an article. """
  @classmethod
  def is_article(cls, word):
    return word in cls.articles

  """ Return substring of input line containing input article and following 
      word. """
  @staticmethod
  def get_article_and_word(line, article):
    # retrieve the substring of the line following the first identified article
    sub_line = line[line.find(article):]
    # if substring contains > 1 space, the space directly next is the end of the string
    if sub_line.count(' ') > 1:
      end_index = sub_line.find(' ', sub_line.find(' ') + 1)
      return sub_line[0:end_index]
    else:
      return sub_line

  """ Write input csv list to input csv file name.  """
  @staticmethod
  def write_body_text_to_csv(csv_list, csv_file_name):
    # return data by retrieving the tag content
    with open(csv_file_name, 'a') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(csv_list)

  """ Return input dataframe split into input chunk_size-sized lists."""
  @staticmethod
  def split_dataframe(dataframe, chunk_size):
    df_list = dataframe.values.flatten().tolist()
    return [df_list[i:i + chunk_size] for i in
            range(0, len(df_list), chunk_size)]

  """ Return csv list containing each entry of input dataframe, cleaned for 
      punctuation and target language. """
  def clean_dataframe(self, dataframe):
    csv_list = []

    for entry in dataframe:
      word = self.cleaner.clean_word(entry)
      if word is not None:
        csv_list.append(word)
    return csv_list

  """ Return clean_dataframe() method call on input dataframe. """
  def worker(self, dataframe):
    return self.clean_dataframe(dataframe)
