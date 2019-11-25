import unittest
import string
from unittest import TestCase
from encryption.Cesar import Cesar


class TestCesar(TestCase):
    # ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    listOfCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    def test_encrypter_output_offset_1(self):
        """
        Tests encryption output with offset 1
        """
        # call with reduced value range
        textData = "~"
        result = Cesar.encrypter(self, 1, textData, self.listOfCharacters)
        self.assertRegex(result, "A")

    def test_encrypter_output_offset_bigger_then_list(self):
        """
        Tests encryption output with offset higher then length of the list (OutOfRange)
        """
        # call with reduced value range
        textData = "A"
        offsetFactor = len(self.listOfCharacters)+1
        result = Cesar.encrypter(self, offsetFactor, textData, self.listOfCharacters)
        self.assertRegex(result, "B")

    def test_list_contains_characters(self):
        """
        Tests if all asked letters are in the string
        """
        textData = "~"
        self.assertIn(textData, self.listOfCharacters)


if __name__ == '__main__':
    unittest.main()