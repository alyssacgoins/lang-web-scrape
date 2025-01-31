from bs4 import BeautifulSoup
import requests as req
from http import HTTPStatus as status

""" Retrieve a list of web text. """
class Retriever:

  # list of German-language articles
  articles_de = ['der', 'die', 'das', 'den', 'dem', 'des', 'ein', 'eine',
              'einer', 'einem', 'einen']

  """ Initialize Retriever instance. """
  def __init__(self, url):
    self.url = url
    self.req = req

  """ Scrapes data from self.url and returns the body text in the form 
    of a string list. """
  def retrieve_body_text(self):
    response_text = self.get_page_text()
    # create BeautifulSoup object with html parser
    soup = BeautifulSoup(response_text, 'html.parser')
    # remove tags
    for data in soup(['style', 'script']):
      data.decompose()
    return self.soup_to_list(soup)

  """ Return scraped data from self.url. """
  def get_page_text(self):
    try:
      response = req.get(self.url)
      # handle an unsuccessful response
      if (response.status_code != status.OK) or (response.text == ''):
        self.handle_unsuccessful_response(response)
      else:
        return response.text
    except req.exceptions.HTTPError as exc:
      raise req.exceptions.HTTPError(exc)

  """ Raises an exception based on the content of input HTTP response. """
  def handle_unsuccessful_response(self, response):
    # if status code is OK but webpage is empty:
    if response.status_code is status.OK:
      raise req.exceptions.HTTPError("Error: " + self.url + " is blank")

    # if status code is not OK:
    else:
      raise req.exceptions.HTTPError("Error [" + str(response.status_code) +
            "] connecting to " + self.url + ". Exiting program.")

  """ Return input BeautifulSoup text in list form. """
  def soup_to_list(self, soup):
    # create string list of body text entries
    body_text_entries = []
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

  """ Return true if input word is an article. """
  @classmethod
  def is_article(cls, word):
    return word in cls.articles_de

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