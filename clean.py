import string

import requests as req
import pandas as pd

def parse_line(word, csv_list):
  if is_valid_word(word):
    cleaned = clean_word(word)
    csv_list.append(cleaned)
    print(cleaned)

def clean_word(word):
  cleaned_word = word
  # remove dash preceding a word
  if word.endswith('-'):
    cleaned_word = word.split('-', 1)[0]
  # remove dash at end of word
  elif word.startswith('-'):
    cleaned_word = word.split('-', 1)[1]
  # remove acronyms separated from word by dash
  elif '-' in word:
    cleaned_word = ''
    for sect in word.split('-'):
      if not sect.isupper():
        cleaned_word += sect

  return cleaned_word

def is_valid_word(word):
  is_valid = True
  # exclude blank entries
  if is_blank_word(word):
    is_valid = False
  # exclude entries of length 1 or 2
  elif is_too_short(word):
    is_valid = False
  # exclude words containing parenthesis
  elif contains_parenthesis(word):
    is_valid = False
  # exclude english words
  # TODO: add a feature in which we specify home language (language to be excluded)
  elif is_english(word):
    is_valid = False
  # exclude ellipses
  elif contains_ellipses(word):
    is_valid = False
  # exclude numbers
  elif contains_number(word):
    is_valid = False
  # exclude phrases that contain no lower-case characters
  elif contains_no_lowercase(word):
    is_valid = False
  # return validity status
  return is_valid

def is_blank_word(word):
  return word == ''

def is_too_short(word):
  return len(word)<3

def contains_parenthesis(word):
  return '(' in word

def contains_ellipses(word):
  return '...' in word or '..' in word

def contains_number(word):
  return any(char.isdigit() for char in word)

def contains_no_lowercase(word):
  return word.isupper()


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

