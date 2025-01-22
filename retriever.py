from bs4 import BeautifulSoup
import requests as req

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
      for word in entry.split():
        body_text_entries.append(word)
    return body_text_entries
  except:
    print()
