import unittest
import os
import csv
import pandas as pd

from src import cleaner, processor

import mockito
from mockito import when

""" Processor unit test. """
class MyTestCase(unittest.TestCase):

  def __init__(self, methodName: str = "runTest"):
    super().__init__(methodName)
    self.mock_cleaner = mockito.mock(cleaner.Cleaner('', ''))
    self.processor_instance = processor.Processor(self.mock_cleaner)

  @classmethod
  def setUpClass(cls):
    # write to sample csv
    with open('sample_files/filled-test-csv.csv', 'w') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(['sample', 'csv', 'text'])

  def test_clear_file_non_empty_file(self):
    self.processor_instance.clear_file('filled-test-csv.csv')
    is_empty = os.stat('sample_files/filled-test-csv.csv').st_size == 0
    self.assertEqual(True, is_empty)

  def test_clear_file_empty_file(self):
    self.processor_instance.clear_file('empty-test-csv.csv')
    is_empty = os.stat('sample_files/empty-test-csv.csv').st_size == 0
    self.assertEqual(True, is_empty)

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
