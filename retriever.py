from bs4 import BeautifulSoup
import requests as req
import csv

articles =   ['der','die', 'das','den','dem','des', 'ein', 'eine', 'einer', 'einem', 'einen']

""" Scrapes data from input webpage and returns the body text in the form of a 
      string list. """
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
      print(entry)
      word_follows_article = False
      for word in entry.split():
        if (word_follows_article):
          word_follows_article = False
          continue
        if (is_article(word)):
          substring = get_article_and_word(entry, word)
          body_text_entries.append(substring)
          word_follows_article = True
        else:
          body_text_entries.append(word)

    # # return data by retrieving the tag content
    with open('retrieved.csv', 'w') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(body_text_entries)
    return body_text_entries
  except:
    print()


def is_article(word):
  return word in articles


def get_article_and_word(line, article):

  # retrieve the substring of the line after first identified article
  sub_line = line[line.find(article):]
  # if article contains >1 space:
  if sub_line.count(' ') >1:
    end_index = sub_line.find(' ', sub_line.find(' ') + 1)
    return sub_line[0:end_index]
  else:
    return sub_line
  # find the next space after the next space, and then attach the next
  # article_and_word =
  # add to the list as a single entry.

def retrieve_word_after_article(line_subset):
  return line_subset