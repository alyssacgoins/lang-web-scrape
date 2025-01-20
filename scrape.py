from bs4 import BeautifulSoup
import requests as req
from clean import parse
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

    count = 0
    for string in soup.stripped_strings:
      count=count+1
      parse(string, csv_input)
      if count>20:
        break

    df = pd.DataFrame(csv_input)
    df2 = df.drop_duplicates()
    print(df2)
    df2.to_csv("final_result.csv", index=False)

  except:
    print("An exception occurred")
