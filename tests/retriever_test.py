import http
import unittest

from bs4 import BeautifulSoup

from src import retriever
import requests as req
import mockito
from mockito import when

""" Retriever unit test. """
class MyTestCase(unittest.TestCase):

  def __init__(self, methodName: str = "runTest"):
    super().__init__(methodName)
    self.retriever_instance = retriever.Retriever('https://test-url')
    self.retriever_instance.req = mockito.mock(req)

  def test_retrieve_body_text_200(self):
    with open('sample_files/sample.html', 'r') as f:
      html_content = f.read()
      when(req).get('https://test-url').thenReturn(
        MockHttpResponse(html_content, http.HTTPStatus.OK))
      body_text_list = self.retriever_instance.retrieve_body_text()
      self.assertEqual(['Heading', 'Sample', 'paragraph.'], body_text_list)

  def test_retrieve_body_text_200_empty(self):
    when(req).get('https://test-url').thenReturn(
      MockHttpResponse('', http.HTTPStatus.OK))
    self.assertRaises(req.exceptions.HTTPError,
                      lambda: self.retriever_instance.retrieve_body_text())

  def test_retrieve_body_text_non_200(self):
    when(req).get('https://test-url').thenReturn(
      MockHttpResponse({}, http.HTTPStatus.FORBIDDEN))
    self.assertRaises(Exception,
                      lambda: self.retriever_instance.retrieve_body_text())

  def test_soup_to_list_success(self):
    with open('sample_files/sample.html', 'r') as f:
      html_content = f.read()
      soup = BeautifulSoup(html_content, 'html.parser')
      body_text_entries = self.retriever_instance.soup_to_list(soup)
      self.assertEqual(['Heading', 'Sample', 'paragraph.'], body_text_entries)

  def test_is_article_false(self):
    is_article = self.retriever_instance.is_article('hallo')
    self.assertEqual(False, is_article)

  def test_is_article_empty(self):
    is_article = self.retriever_instance.is_article('')
    self.assertEqual(False, is_article)

  def test_is_article_de(self):
    articles = ['der', 'die', 'das', 'den', 'dem', 'des', 'ein', 'eine',
                'einer', 'einem', 'einen']
    for article in articles:
      is_article = self.retriever_instance.is_article(article)
      self.assertEqual(True, is_article)

  def test_get_article_and_word_single_pair(self):
    article_and_word = self.retriever_instance.get_article_and_word(
      'die Katze', 'die')
    self.assertEqual('die Katze', article_and_word)

  def test_get_article_and_word_end_pair(self):
    article_and_word = self.retriever_instance.get_article_and_word(
      'und die Katze', 'die')
    self.assertEqual('die Katze', article_and_word)

  def test_get_article_and_word_start_pair(self):
    article_and_word = self.retriever_instance.get_article_and_word(
      'die Katze sind', 'die')
    self.assertEqual('die Katze', article_and_word)


if __name__ == '__main__':
  unittest.main()

""" Mock HttpResponse used for testing. """
class MockHttpResponse:
  def __init__(self, text, status_code):
    self.text = text
    self.status_code = status_code

  def json(self):
    return self.text
