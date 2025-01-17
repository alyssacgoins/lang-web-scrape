from bs4 import BeautifulSoup
import requests as req
import csv
from clean import parse, rem_duplicates

""" Scrapes data from input webpage and saves body text to csv. """
def scrape(page):
  # Retrieve html data from input webpage
  try:
    web = req.get(page)

    # Create BeautifulSoup object and specify parser
    soup = BeautifulSoup(web.text, "html.parser")

    # Remove tags
    for data in soup(['style', 'script']):
      data.decompose()

    # Create string list of body text entries
    csv_input = ['']
    for string in soup.stripped_strings:
      # csv_input.append(string)
      parse(string, csv_input)

    # Write list to csv file
    with open('body-text.csv', 'w') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(csv_input)
    rem_duplicates()
  except:
    print("An exception occurred")
