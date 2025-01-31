import string
import unittest
from src import cleaner

""" Unit test for cleaner.py """
class MyTestCase(unittest.TestCase):

  def __init__(self, methodName: str = "runTest"):
    super().__init__(methodName)
    self.cleaner_instance = cleaner.Cleaner('DE', 'EN')

  def test_remove_non_ascii_no_punctuation(self):
    word = 'hallo'
    cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
    self.assertEqual('hallo', cleaned_ascii)

  def test_remove_first_last_non_ascii_characters(self):
    # iterate through all symbols
    for symbol in (
        string.punctuation + self.cleaner_instance.non_library_punctuation):

      # case in which word starts with given symbol
      start_symbol = symbol + 'hallo'
      cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(
        start_symbol)
      self.assertEqual('hallo', cleaned_ascii)

      # case in which word ends with given symbol
      end_symbol = 'hallo' + symbol
      cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(
        end_symbol)
      self.assertEqual('hallo', cleaned_ascii)

  def test_remove_nbsp_contains_no_nbsp(self):
    word = 'hallo'
    cleaned_ascii = self.cleaner_instance.remove_nbsp(word)
    self.assertEqual('hallo', cleaned_ascii)

  def test_remove_nbsp_contains_start_nbsp(self):
    word = '\u00A0hallo'
    cleaned_ascii = self.cleaner_instance.remove_nbsp(word)
    self.assertEqual('hallo', cleaned_ascii)

  # todo add a case to elif no interior chars - acc for this.
  def test_remove_nbsp_contains_interior_nbsp(self):
    word = 'ha\u00A0llo'
    cleaned_ascii = self.cleaner_instance.remove_nbsp(word)
    self.assertEqual('hallo', cleaned_ascii)

  def test_remove_nbsp_contains_end_nbsp(self):
    word = 'hallo\u00A0'
    cleaned_ascii = self.cleaner_instance.remove_nbsp(word)
    self.assertEqual('hallo', cleaned_ascii)

  def test_is_valid_word_yes(self):
    word = 'hallo'
    is_valid = self.cleaner_instance.is_valid_word(word)
    self.assertEqual(True, is_valid)

  def test_is_valid_word_empty(self):
    word = ''
    is_valid = self.cleaner_instance.is_valid_word(word)
    self.assertEqual(False, is_valid)

  def test_is_valid_word_blank(self):
    word = ' '
    is_valid = self.cleaner_instance.is_valid_word(word)
    self.assertEqual(False, is_valid)

  def test_is_valid_word_short(self):
    word = 'im'
    is_valid = self.cleaner_instance.is_valid_word(word)
    self.assertEqual(False, is_valid)

  def test_is_valid_word_contains_num(self):
    word = 'h5allo'
    is_valid = self.cleaner_instance.is_valid_word(word)
    self.assertEqual(False, is_valid)

  def test_is_valid_word_starts_num(self):
    word = '6Hallo'
    is_valid = self.cleaner_instance.is_valid_word(word)
    self.assertEqual(False, is_valid)

  def test_is_valid_word_ends_num(self):
    word = 'hallo9'
    is_valid = self.cleaner_instance.is_valid_word(word)
    self.assertEqual(False, is_valid)

  def test_is_valid_word_all_uppercase(self):
    word = 'HALLO'
    is_valid = self.cleaner_instance.is_valid_word(word)
    self.assertEqual(False, is_valid)

  def test_is_valid_word_consec_uppercase(self):
    word = 'HAllo'
    is_valid = self.cleaner_instance.is_valid_word(word)
    self.assertEqual(False, is_valid)

  def test_is_valid_word_interior_symbol(self):
    # iterate through all symbols
    for symbol in ['!', '#', '$', '€', '%', '&', '(', ')', '+', '.', '/',
                     ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
                     '_', '`', '{', '|', '}', '~', ',', '„', '“', '»']:

      # case in which word starts with given symbol
      word = 'ha' + symbol + 'llo'
      is_valid = self.cleaner_instance.is_valid_word(
        word)
      self.assertEqual(False, is_valid)

if __name__ == '__main__':
  unittest.main()
