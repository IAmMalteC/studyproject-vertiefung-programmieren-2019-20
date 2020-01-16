import unittest
import string
from unittest import TestCase
from encryption.Cesar import encrypter


class TestCesar(TestCase):
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    def test_encrypter_output_offset_1(self):
        """
        Tests encryption output with offset 1
        call with reduced value range
        """
        text_data = "~"
        result = encrypter(1, text_data, self.list_of_characters)
        self.assertRegex(result, "a")

    def test_encrypter_output_offset_bigger_then_list(self):
        """
        Tests encryption output with offset higher then length of the list (OutOfRange)
        call with reduced value range
        """
        text_data = "a"
        offset_factor = len(self.list_of_characters) + 1
        result = encrypter(offset_factor, text_data, self.list_of_characters)
        self.assertRegex(result, "b")

    def test_list_contains_characters(self):
        """
        Tests if all asked letters are in the string
        call with reduced value range
        """
        text_data = "~"
        self.assertIn(text_data, self.list_of_characters)


if __name__ == '__main__':
    unittest.main()