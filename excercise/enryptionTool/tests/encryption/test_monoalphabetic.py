import unittest
import string
from unittest import TestCase
from encryption.MonoAlphabetic import mono_encrypter, reverse_text


class TestMonoAlphabetic(TestCase):
    list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    # monoAlphabetic = MonoAlphabetic()
    list_of_characters_reverse = reverse_text(list_of_characters)

    def test_encrypter(self):
        """
        Tests the encryption
        call with reduced value range
        """
        text_data = "a"
        result = mono_encrypter(text_data, self.list_of_characters, self.list_of_characters_reverse)
        self.assertRegex(result, "~")

    def test_reverse_text(self):
        """
        Tests it the text is reversed
        call with reduced value range
        """
        text_data = "abcd"
        result = reverse_text(text_data)
        self.assertEqual(result, "dcba")


if __name__ == '__main__':
    unittest.main()
