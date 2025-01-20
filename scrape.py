from bs4 import BeautifulSoup
import requests as req
from clean import parse_line
import pandas as pd

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
      for word in string.split():
        csv_input.append(word)

    df = pd.DataFrame(csv_input)
    df2 = df.drop_duplicates()

    csv_input = ['']
    for row in df2.iterrows():
      parse_line(row[1][0], csv_input)

    df2.to_csv("final_result.csv", index=False)
  #
  except:
    print("An exception occurred")
