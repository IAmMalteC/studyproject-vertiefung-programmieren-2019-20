import unittest
from unittest import TestCase
from userinput import offset


class TestOffset(TestCase):
    def test_if_number_is_returned(self):
        """
        Tests if it returns the given number
        :return: int offset_factor
        """
        number = offset.get_offset(10)
        self.assertEqual(number, 10)

    def test_if_random_number_is_returned_given_text(self):
        """
        Tests if it returns a random number, when a text is given
        :return: int offset_factor
        """
        number = offset.get_offset("abc")
        self.assertIs(type(number), int)

    def test_if_random_number_is_returned_given_float(self):
        """
        Tests if it returns a random number, when a floatnumber is given
        :return: int offset_factor
        """
        number = offset.get_offset(1.4)
        self.assertIs(type(number), int)

if __name__ == '__main__':
    unittest.main()