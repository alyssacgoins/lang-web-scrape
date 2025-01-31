import unittest
import cleaner

""" Unit test for cleaner.py """
class MyTestCase(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.cleaner_instance = cleaner.Cleaner('DE', 'EN')

    def test_remove_non_ascii_no_punctuation(self):
        word = 'hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_exclamation(self):
        word = '!hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_exclamation(self):
        word = 'hallo!'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_hash(self):
        word = '#hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_hash(self):
        word = 'hallo#'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_dollar(self):
        word = '$hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_dollar(self):
        word = 'hallo$'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_euro(self):
        word = '€hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_euro(self):
        word = 'hallo€'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_percent(self):
        word = '%hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_percent(self):
        word = 'hallo%'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_ampersand(self):
        word = '&hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_ampersand(self):
        word = 'hallo&'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_open_parenthesis(self):
        word = '(hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_open_parenthesis(self):
        word = 'hallo('
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_close_parenthesis(self):
        word = ')hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_close_parenthesis(self):
        word = 'hallo)'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_plus(self):
        word = '+hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_plus(self):
        word = 'hallo+'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_period(self):
        word = '.hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_period(self):
        word = 'hallo.'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_forward_dash(self):
        word = '/hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_forward_dash(self):
        word = 'hallo/'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_colon(self):
        word = 'hallo:'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_colon(self):
        word = ':hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_semicolon(self):
        word = ';hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_semicolon(self):
        word = 'hallo;'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_less_than(self):
        word = '<hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_less_than(self):
        word = 'hallo<'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_equals(self):
        word = '=hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_equals(self):
        word = 'hallo='
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_greater_than(self):
        word = '>hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_grwater_than(self):
        word = 'hallo>'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_question(self):
        word = '?hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_question(self):
        word = 'hallo?'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_address(self):
        word = '@hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_address(self):
        word = 'hallo@'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_open_bracket(self):
        word = '[hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_open_bracket(self):
        word = 'hallo['
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_close_bracket(self):
        word = ']hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_close_bracket(self):
        word = 'hallo]'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_back_dash(self):
        word = '\\hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_back_dash(self):
        word = 'hallo\\'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_carrot(self):
        word = '^hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_carrot(self):
        word = 'hallo^'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_underscore(self):
        word = '_hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_underscore(self):
        word = 'hallo_'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_backtick(self):
        word = '`hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_backtick(self):
        word = 'hallo`'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_open_brace(self):
        word = '{hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_open_brace(self):
        word = 'hallo{'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_close_brace(self):
        word = '}hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_close_brace(self):
        word = 'hallo}'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_pipe(self):
        word = '|hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_pipe(self):
        word = 'hallo|'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_tilde(self):
        word = '~hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_tilde(self):
        word = 'hallo~'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_comma(self):
        word = ',hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_comma(self):
        word = 'hallo,'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_bottom_quote(self):
        word = '„hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_bottom_quote(self):
        word = 'hallo„'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_top_quote(self):
        word = '“hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_top_quote(self):
        word = 'hallo“'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_start_guillemet(self):
        word = '»hallo'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
        self.assertEqual('hallo', cleaned_ascii)

    def test_remove_non_ascii_end_guillemet(self):
        word = 'hallo»'
        cleaned_ascii = self.cleaner_instance.remove_first_last_non_ascii(word)
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

    """ Validate and clean input word and append to input list. """
    def test_is_valid_word_yes(self):
        word = 'hallo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(True, is_valid)

    """ Validate and clean input word and append to input list. """
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

    # todo: is_src_lang testing, stub?

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

    def test_is_valid_word_interior_exclamation(self):
        word = 'Ha!llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_hash(self):
        word = 'Ha#llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_dollar(self):
        word = 'Ha$llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_euro(self):
        word = 'Ha€llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_percentage(self):
        word = 'Ha%llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_ampersand(self):
        word = 'Ha&llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_open_parenthesis(self):
        word = 'Ha(llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_close_parenthesis(self):
        word = 'Ha)llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_plus_sign(self):
        word = 'Ha+llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_period(self):
        word = 'Ha.llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_forward_dash(self):
        word = 'Ha/llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_colon(self):
        word = 'Ha:llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_semicolon(self):
        word = 'Ha;llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_less_than(self):
        word = 'Ha<llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_equals(self):
        word = 'Ha=llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_greater_than(self):
        word = 'Ha>llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_question_mark(self):
        word = 'Ha?llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_address_sign(self):
        word = 'Ha@llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_open_bracket(self):
        word = 'Ha[llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_back_dash(self):
        word = 'Ha\\llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_close_bracket(self):
        word = 'Ha]llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_carrot(self):
        word = 'Ha^llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_underscore(self):
        word = 'Ha_llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_backtick(self):
        word = 'Ha`llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_open_brace(self):
        word = 'Ha{llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_pipe(self):
        word = 'Ha|llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_close_brace(self):
        word = 'Ha}llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_tilde(self):
        word = 'Ha~llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_comma(self):
        word = 'Ha,llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_bottom_quote(self):
        word = 'Ha„llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_top_quote(self):
        word = 'Ha“llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_guillemet(self):
        word = 'Ha»llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

if __name__ == '__main__':
    unittest.main()
