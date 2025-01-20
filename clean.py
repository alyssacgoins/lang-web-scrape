import string

import requests as req
import pandas as pd

""" Validate and clean input word and append to input list. """
def process_word(word, csv_list):
  if is_valid_word(word):
    cleaned = rem_punctuation(word)
    csv_list.append(cleaned)
    print(cleaned)

""" Return true if input word is valid according to the conditions below. """
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
  elif is_entirely_uppercase(word):
    is_valid = False
  # return validity status
  return is_valid

""" Return input word with all punctuation removed. """
def rem_punctuation(word):
  cleaned_word = word
  for char in word:
    if char in string.punctuation:
      cleaned_word = rem_symbol(cleaned_word, char)
  return cleaned_word


""" Return input word with all instances of input symbol removed. """
def rem_symbol(word, symbol):
  cleaned_word = word
  # remove dash preceding a word
  if word.endswith(symbol):
    cleaned_word = word.split(symbol, 1)[0]
  # remove dash at end of word
  elif word.startswith(symbol):
    cleaned_word = word.split(symbol, 1)[1]
  # remove acronyms separated from word by dash
  elif symbol in word:
    cleaned_word = ''
    for sect in word.split(symbol):
      if not sect.isupper():
        cleaned_word += sect

  return cleaned_word

""" Return true if input word is empty string. """
def is_blank_word(word):
  return word == ''

""" Return true if input word is shorter than three characters. """
def is_too_short(word):
  return len(word)<3

#todo this is unecessary now that we do a full punctuation check.
""" ------ """
def contains_parenthesis(word):
  return '(' in word

#todo this is unecessary now that we do a full punctuation check.
def contains_ellipses(word):
  return '...' in word or '..' in word

""" Return true if input word contains a number. """
def contains_number(word):
  return any(char.isdigit() for char in word)

""" Return true if input word is entirely uppercase. """
#todo is this extra method call necessary?
def is_entirely_uppercase(word):
  return word.isupper()


""" Executes API call to merriam-webster dictionary API to determine if 
    word is English. """
def is_english(line):
  try:
    header_info = {'app_id': '3d637214', 'app_key': '',
              'Accept': 'application/json'}
    url = "https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/en-gb/" + line
    web = req.get(url=url, headers=header_info)
    return web.ok
  except:
    print("An exception occurred processing english dictionary entry")
    return False

