import string
import requests as req

""" Clean html body text. """
class Cleaner:

  """ Initialize Cleaner instance. """
  def __init__(self, src, target):
    self.src_lang = src
    self.target_lang = target

  # non-breaking space
  nbsp = '\u00A0'
  # empty space
  space = ' '
  # additional punctuation not included in string.punctuation library.
  non_library_punctuation = '„“»€'

  """ Validate and clean input word and append to input list. """
  def clean_word(self, word):
    cleaned = ''
    if self.is_valid_word(word):
      # if valid word, remove any punctuation at start/end & any nbsp
      cleaned = self.remove_nbsp(self.remove_first_last_non_ascii(word))
      print(cleaned)
    return cleaned

  """ Return true if input word is valid according to the conditions below. """
  def is_valid_word(self, word):
    is_valid = True

    # exclude words that are blank
    if self.is_blank_word(word):
      is_valid = False
    # exclude words of length < 3
    elif self.is_too_short(word):
      is_valid = False
    # exclude words in source language
    elif self.is_src_lang(word):
      is_valid = False
    # exclude words containing numbers
    elif self.contains_number(word):
      is_valid = False
    # exclude words in all-caps
    elif self.contains_all_uppercase(word):
      is_valid = False
    # exclude words with two or more consecutive uppercase
    elif self.contains_consecutive_uppercase_no_symbol(word):
      is_valid = False
    # exclude words split by punctuation
    elif self.contains_interior_punctuation(word):
      is_valid = False
    # return validity status
    return is_valid

  """ Return true if interior of input word contains punctuation (non-asterisk 
      or dash)."""
  @staticmethod
  def contains_interior_punctuation(word):
    contains = False

    valid_symbols = ['!', '#', '$', '€', '%', '&', '(', ')', '+', '.', '/',
                     ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
                     '_', '`', '{', '|', '}', '~', ',', '„', '“', '»']

    if len(word) >2:
      # check for punctuation that appears within a word
      for char in word[1:-1]:
        if char in valid_symbols:
          contains = True
          break
    return contains

  """ Return input word with non-ascii characters removed. """
  @classmethod
  def remove_first_last_non_ascii(cls, word):
    cleaned_word = word

    for char in word:
      if (char in string.punctuation) or (char in cls.non_library_punctuation):
        cleaned_word = cls.remove_symbol(cleaned_word, char)
    return cleaned_word

  @classmethod
  def remove_nbsp(cls, word):
    return word.replace(cls.nbsp, '')


  """ Return input word with all instances of input symbol removed. """
  @staticmethod
  def remove_symbol(word, symbol):
    cleaned_word = word

    # remove symbol preceding a word
    if word.startswith(symbol):
      cleaned_word = word.split(symbol, 1)[1]
    # remove symbol at end of word
    elif word.endswith(symbol):
      cleaned_word = word.split(symbol, 1)[0]
    # remove acronyms separated from word by symbol, as well as symbol
    elif symbol in word:
      cleaned_word = ''
      for sect in word.split(symbol):
        if not sect.isupper():
          cleaned_word += sect

    return cleaned_word

  """ Return true if input word is empty string. """
  @staticmethod
  def is_blank_word(word):
    return word == ''

  """ Return true if input word is shorter than three characters. """
  @staticmethod
  def is_too_short(word):
    return len(word) < 3

  """ Return true if input word contains a number. """
  @staticmethod
  def contains_number(word):
    return any(char.isdigit() for char in word)

  """ Return true if input word is entirely uppercase. """
  # todo is this extra method call necessary?
  @staticmethod
  def contains_all_uppercase(word):
    return word.isupper()

  # todo adapt to multi-lang dictionaries
  """ Return true if word is English. """
  def is_src_lang(self, word):
    lang = self.src_lang
    # todo fix english dictionary http
    #return self.get_english(word) == True
    return False

  """ Executes API call to merriam-webster dictionary API for input word. """
  @staticmethod
  def get_english(word):
    try:
      header_info = {'app_id': '3d637214', 'app_key': '',
                     'Accept': 'application/json'}
      url = (
            "https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/en-gb/"
            + word)
      web = req.get(url=url, headers=header_info)
      return web.ok
    except Exception as exc:
      print("An exception occurred processing english dictionary entry", exc)
      return False

  """ Return true if input word contains consecutive uppercase characters, and 
      no symbol. (e.g. HRT-hallo would return false). """
  @staticmethod
  def contains_consecutive_uppercase_no_symbol(word):
    contains = False

    for i in (0, len(word) - 2):
      if word[i].isupper() and word[i + 1].isupper():
        contains = True
    return contains
