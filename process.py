from scrape import scrape_body_text
from scrape import handle_body_text
import csv

def process(url):
  csv_list = handle_body_text(scrape_body_text(url))

  # return data by retrieving the tag content
  with open('final_result.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_list)