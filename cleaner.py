import string
import requests as req

special_quotes = ['„', '“', '»']


""" Validate and clean input word and append to input list. """
def process_word(word, csv_list):
  if is_valid_word(word):
    # todo handle NC-djlbsdc should return djlbsdc
    cleaned = remove_acronyms(word)
    cleaned = remove_punctuation(cleaned)
    csv_list.append(cleaned)
    print(cleaned)
  return csv_list

def remove_acronyms(word):
  return word


""" Return true if input word is valid according to the conditions below. """
def is_valid_word(word):
  is_valid = True
  # exclude blank entries
  if is_blank_word(word):
    is_valid = False
  # exclude entries of length 1 or 2
  elif is_too_short(word):
    is_valid = False
  # exclude english words
  # TODO: add a feature in which we specify home language (language to be excluded)
  elif is_english(word):
    is_valid = False
  # exclude numbers
  elif contains_number(word):
    is_valid = False
  # exclude phrases that contain no lower-case characters
  #todo handle NC-djlbsdc should return djlbsdc
  elif contains_all_uppercase(word):
    is_valid = False
  elif contains_consecutive_uppercase(word):
    is_valid = False
  elif contains_interior_punctuation(word):
    is_valid = False
  # return validity status
  return is_valid



""" Return true if interior of input word contains punctuation (non-asterisk 
    or dash)."""
def contains_interior_punctuation(word):
  contains = False

  spec_punc = ['!', '#', '$', '%', '&', '(', ')', '+','', '.', '/', ':', ';',
  '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{','|', '}', '~', ',']
  for char in word:
    if char in spec_punc:
      contains = True
  return contains


""" Return input word with all punctuation removed. """
def remove_punctuation(word):
  cleaned_word = word
  for char in word:
    if (char in string.punctuation) or (char in special_quotes):
      cleaned_word = remove_symbol(cleaned_word, char)
  return cleaned_word


""" Return input word with all instances of input symbol removed. """
def remove_symbol(word, symbol):
  cleaned_word = word
  # remove symbol preceding a word
  if word.endswith(symbol):
    cleaned_word = word.split(symbol, 1)[0]
  # remove symbol at end of word
  elif word.startswith(symbol):
    cleaned_word = word.split(symbol, 1)[1]
  # remove acronyms separated from word by symbol, as well as symbol
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
  return len(word) < 3

""" Return true if input word contains a number. """
def contains_number(word):
  return any(char.isdigit() for char in word)


""" Return true if input word is entirely uppercase. """
# todo is this extra method call necessary?
def contains_all_uppercase(word):
  return word.isupper()


""" Return true if word is English. """
def is_english(word):
  return get_english==True


""" Executes API call to merriam-webster dictionary API for input word. """
def get_english(word):
  try:
    header_info = {'app_id': '3d637214', 'app_key': '',
                   'Accept': 'application/json'}
    url = ("https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/en-gb/"
           + word)
    web = req.get(url=url, headers=header_info)
    return web.ok
  except:
    print("An exception occurred processing english dictionary entry")
    return False


""" Return true if input word contains consecutive uppercase characters. """
def contains_consecutive_uppercase(word):
  contains = False
  for i in (0, len(word) -2):
    if word[i].isupper() and word[i+1].isupper():
      contains = True
  return contains