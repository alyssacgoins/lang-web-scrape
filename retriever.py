from bs4 import BeautifulSoup
import requests as req

""" Retrieve web text. """
class Retriever:

  """ Initialize Retriever instance. """
  def __init__(self, url):
    self.url = url

  """ Scrapes data from instance webpage and returns the body text in the form 
    of a string list. """
  def retrieve_body_text(self):
    try:
      response = req.get(self.url)

      # create BeautifulSoup object with html parser
      soup = BeautifulSoup(response.text, 'html.parser')
      # remove tags
      for data in soup(['style', 'script']):
        data.decompose()
      return soup
    except Exception as exc:
      raise Exception(exc)
