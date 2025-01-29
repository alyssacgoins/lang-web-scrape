import unittest
import cleaner

""" Unit test for cleaner.py """
class MyTestCase(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.cleaner_instance = cleaner.Cleaner('DE', 'EN')

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

    def test_is_valid_word_interior_exclamation_pt(self):
        word = 'Ha!llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_hash(self):
        word = 'Ha#llo'
        is_valid = self.cleaner_instance.is_valid_word(word)
        self.assertEqual(False, is_valid)

    def test_is_valid_word_interior_dollar_sign(self):
        word = 'Ha$llo'
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

if __name__ == '__main__':
    unittest.main()
