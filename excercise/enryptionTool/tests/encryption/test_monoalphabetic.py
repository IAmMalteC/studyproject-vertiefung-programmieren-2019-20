import unittest
import string
from unittest import TestCase
from encryption.Monoalphabetic import Monoalphabetic

class TestMonoalphabetic(TestCase):
    list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    list_of_characters_reverse = Monoalphabetic.reverse_text(list_of_characters)

    def test_encoder(self):
        """
        Tests the encoding
        """
        text_data = "A"
        result = Monoalphabetic.encoder(self, text_data, self.list_of_characters, self.list_of_characters_reverse)
        self.assertRegex(result, "~")

    def test_reverse_text(self):
        """
        Tests it the text is reversed
        """
        text_data = "abcd"
        result = Monoalphabetic.reverse_text(text_data)
        self.assertEqual(result,"dcba")

if __name__ == '__main__':
    unittest.main()