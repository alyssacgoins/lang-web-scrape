from scrape import scrape_body_text
from scrape import handle_body_text
def worker(body_text_entries):
  print("Worker thread running")
  handle_body_text(body_text_entries)

def process(url):
  handle_body_text(scrape_body_text(url))


