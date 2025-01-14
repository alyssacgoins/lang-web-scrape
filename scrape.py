from bs4 import BeautifulSoup
import requests as req
import csv
import array as arr

""" Scrapes data from input webpage and saves body text to csv. """
def scrape(page):
  # Requesting for the website
  web = req.get(page)

  # Creating a BeautifulSoup object and specifying the parser
  soup = BeautifulSoup(web.text, "html.parser")

  for data in soup(['style', 'script']):
    # Remove tags
    data.decompose()

  input_var = ['']
  for x in soup.stripped_strings:
    input_var.append(x)

  # # return data by retrieving the tag content
  with open('body-text.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(input_var)
