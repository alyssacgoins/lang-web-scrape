import requests as req
import pandas as pd

""" Parse  """
def parse(line, csv_list):
  # Exclude empty lines
  if line == '':
    print("Blank entry: not adding this line")
    return
  # Exclude words/phrase containing parenthesis
  elif '(' in line:
    print("Parenthesis: not adding this line")
    return
  # Exclude 2-letter words
  elif len(line) <3:
    print("Length less than 3: not adding this line")
    return
  # Exclude words in English
  # TODO: add a feature in which we specify home language (language to be excluded)
  elif is_english(line):
    print("Word is English: not adding this line")
    return
  elif '..' in line:
    print("Two dots: not adding this line")
    return
  else:
    print("Adding.")
    for word in line.split():
      csv_list.append(word)

""" Executes API call to merriam-webster dictionary API to determine if 
    word is English. """
def is_english(line):
  try:
    header_info = {'app_id': '3d637214', 'app_key': '967ae2663b05f2416916bd5c712d9d21',
              'Accept': 'application/json'}
    url = "https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/en-gb/" + line
    web = req.get(url=url, headers=header_info)
    return web.ok
  except:
    print("An exception occurred processing english dictionary entry")
    return False

""" Removes duplicates from cleaned csv. """
def rem_duplicates():
  df = pd.read_csv("body-text.csv")
  df.drop_duplicates(keep='first', )
  df.to_csv("final_result.csv")
