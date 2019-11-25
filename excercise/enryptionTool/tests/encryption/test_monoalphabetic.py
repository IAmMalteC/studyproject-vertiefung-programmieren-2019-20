import unittest
import string
from unittest import TestCase
from encryption.Monoalphabetic import Monoalphabetic

class TestMonoalphabetic(TestCase):
    listOfCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    listOfCharactersReverse = Monoalphabetic.reverse_text(listOfCharacters)

    def test_encrypter(self):
        """
        Tests the encoding
        """
        textData = "A"
        result = Monoalphabetic.encrypter(self, textData, self.listOfCharacters, self.listOfCharactersReverse)
        self.assertRegex(result, "~")

    def test_reverse_text(self):
        """
        Tests it the text is reversed
        """
        textData = "abcd"
        result = Monoalphabetic.reverse_text(textData)
        self.assertEqual(result,"dcba")

if __name__ == '__main__':
    unittest.main()