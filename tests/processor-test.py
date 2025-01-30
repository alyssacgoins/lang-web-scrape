import unittest
import os
import csv
import pandas as pd

import processor
import cleaner

import mockito
from mockito import when


class MyTestCase(unittest.TestCase):

  def __init__(self, methodName: str = "runTest"):
    super().__init__(methodName)
    self.mock_cleaner = mockito.mock(cleaner.Cleaner('', ''))
    self.processor_instance = processor.Processor(self.mock_cleaner)


  @classmethod
  def setUpClass(cls):
    # write to sample csv
    with open('filled-test-csv.csv', 'w') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(['sample', 'csv', 'text'])

  def test_clear_file_non_empty_file(self):
    self.processor_instance.clear_file('filled-test-csv.csv')
    is_empty = os.stat('filled-test-csv.csv').st_size == 0
    self.assertEqual(True, is_empty)

  def test_clear_file_empty_file(self):
    self.processor_instance.clear_file('empty-test-csv.csv')
    is_empty = os.stat('empty-test-csv.csv').st_size == 0
    self.assertEqual(True, is_empty)

#todo mock soup object
  # """ Handle case of empty soup. """
  # def test_soup_to_list_empty(self):
  #   self.processor_instance.soup_to_list()

  def test_split_dataframe_empty(self):
    # set up sample dataframe with an empty list
    dataframe = pd.DataFrame()
    test_list = self.processor_instance.split_dataframe_to_lists(dataframe, 100)
    self.assertEqual(0, len(test_list))

  def test_split_dataframe_filled(self):
    # set up sample dataframe, size 400
    dataframe = pd.DataFrame(['sample'] * 400)
    test_list = self.processor_instance.split_dataframe_to_lists(dataframe, 100)
    self.assertEqual(4, len(test_list))

  def test_split_dataframe_less_than_chunk(self):
    # set up sample dataframe, size 90
    dataframe = pd.DataFrame(['sample'] * 90)
    test_list = self.processor_instance.split_dataframe_to_lists(dataframe, 100)
    self.assertEqual(1, len(test_list))

  def test_is_article_false(self):
    is_article = self.processor_instance.is_article('hallo')
    self.assertEqual(False, is_article)

  def test_is_article_empty(self):
    is_article = self.processor_instance.is_article('')
    self.assertEqual(False, is_article)

  def test_is_article_de(self):
    articles = ['der', 'die', 'das', 'den', 'dem', 'des', 'ein', 'eine',
                'einer', 'einem', 'einen']
    for article in articles:
      is_article = self.processor_instance.is_article(article)
      self.assertEqual(True, is_article)

  def test_get_article_and_word_single_pair(self):
    article_and_word = self.processor_instance.get_article_and_word(
      'die Katze', 'die')
    self.assertEqual('die Katze', article_and_word)

  def test_get_article_and_word_end_pair(self):
    article_and_word = self.processor_instance.get_article_and_word(
      'und die Katze', 'die')
    self.assertEqual('die Katze', article_and_word)

  def test_get_article_and_word_start_pair(self):
    article_and_word = self.processor_instance.get_article_and_word(
      'die Katze sind', 'die')
    self.assertEqual('die Katze', article_and_word)

  def test_clean_list_full(self):
    test_list = ['hallo!', 'i\\&ch', 'BIn', '*eine', '\u00A0gut', 'frau....']

    when(self.mock_cleaner).clean_word('hallo!').thenReturn('hallo')
    when(self.mock_cleaner).clean_word('i\\&ch').thenReturn('')
    when(self.mock_cleaner).clean_word('BIn').thenReturn('bin')
    when(self.mock_cleaner).clean_word('*eine').thenReturn('eine')
    when(self.mock_cleaner).clean_word('\u00A0gut').thenReturn('gut')
    when(self.mock_cleaner).clean_word('frau....').thenReturn('frau')

    clean_list = self.processor_instance.clean_list(test_list)
    self.assertEqual(['hallo', 'bin', 'eine', 'gut', 'frau'], clean_list)

  def clean_list_empty(self):
    test_list = []
    when(self.mock_cleaner).clean_word('').thenReturn('')

    clean_list = self.processor_instance.clean_list(test_list)
    self.processor_instance.clean_list(test_list)
    self.assertEqual([], clean_list)

if __name__ == '__main__':
  unittest.main()
