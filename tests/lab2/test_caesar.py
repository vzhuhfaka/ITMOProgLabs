import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class CalculatorTestCase(unittest.TestCase):

    def test_encrypt_caesar_3(self):
        self.assertEqual(encrypt_caesar('Hello world!', 3), 'Khoor zruog!')

    def test_encrypt_caesar_15(self):
        self.assertEqual(encrypt_caesar('Hello world!', 15), 'Wtaad ldgas!')

    def test_decrypt_caesar_3(self):
        self.assertEqual(decrypt_caesar('Khoor zruog!', 3), 'Hello world!')

    def test_decrypt_caesar_15(self):
        self.assertEqual(decrypt_caesar('Wtaad ldgas!', 15), 'Hello world!')