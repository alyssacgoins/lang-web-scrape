from cleaner import process_word
from retriever import scrape_body_text
import concurrent.futures
import pandas as pd
import csv

# List containing German-language articles
articles =   ['der','die', 'das','den','dem','des', 'ein', 'eine', 'einer',
              'einem', 'einen']


""" Call processing functions """
def process(url):
  body_text = soup_to_list(scrape_body_text(url))
  # clear csv files
  [clear_file(file) for file in ['body-text.csv', 'finally.csv']]
  process_body_text(body_text)
  remove_nbsp('body-text.csv')


""" Clear the contents of the file at input filename. """
def clear_file(file_name):
  f = open(file_name, 'w')
  f.truncate()
  f.close()


""" Return input BeautifulSoup text in list form. """
def soup_to_list(soup):
  # create string list of body text entries
  body_text_entries = ['']
  for entry in soup.stripped_strings:

    word_follows_article = False
    for word in entry.split():
      # if word directly follows an article, skip
      if word_follows_article:
        word_follows_article = False
        continue
      # if word is article, retrieve following word & append to list
      if is_article(word):
        substring = get_article_and_word(entry, word)
        body_text_entries.append(substring)
        word_follows_article = True
      # append word to list
      else:
        body_text_entries.append(word)

  return body_text_entries


""" Execute concurrent cleaning for input body_text_entries and write data to
    csv file. """
def process_body_text(body_text_entries):
  # remove duplicate words via pandas DataFrame
  dataframe = pd.DataFrame(body_text_entries)
  dataframe = dataframe.drop_duplicates()
  # split dataframe
  chunks = split_data(dataframe, 10)

  with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = list(executor.map(worker,chunks))
    for future in futures:
      try:
        write_body_text_to_csv(future, 'body-text.csv')
      except Exception as exc:
        print(f"Source generated an exception")


""" Return true if input word is an article. """
def is_article(word):
  return word in articles


""" Return substring of input line containing input article and corresponding 
    word. """
def get_article_and_word(line, article):
  # retrieve the substring of the line after first identified article
  sub_line = line[line.find(article):]
  # if article contains >1 space:
  if sub_line.count(' ') >1:
    end_index = sub_line.find(' ', sub_line.find(' ') + 1)
    return sub_line[0:end_index]
  else:
    return sub_line


""" Write input csv list to input csv file name.  """
def write_body_text_to_csv(csv_list, csv_file_name):
  # return data by retrieving the tag content
  with open(csv_file_name, 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_list)

def remove_nbsp(csv_file_name):
  with open(csv_file_name, 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)

    for row in rows:
      row = (x.replace('\u00A0', ' ') for x in row)
      with open ('finally.csv', 'a') as final:
        writer = csv.writer(final)
        writer.writerow(row)


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
