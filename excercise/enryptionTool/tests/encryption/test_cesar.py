from unittest import TestCase


class TestCesar(TestCase):
    def setUp(self):
        #call with reduced value range
        self.encrypter = (Cesar("abcd"))
