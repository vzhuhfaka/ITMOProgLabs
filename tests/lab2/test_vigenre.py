import unittest

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class CalculatorTestCase(unittest.TestCase):

    def test_encrypt_vigenre_1(self):
        self.assertEqual(encrypt_vigenere('python', 'dnj'), 'slckbw')

    def test_encrypt_vigenre_2(self):
        self.assertEqual(encrypt_vigenere('sfkjlwje', 'hhem'), 'zmovsdnq')

    def test_encrypt_vigenre_3(self):
        self.assertEqual(encrypt_vigenere('GHIUDFJGKJNKERDFCB', 'MMJRNNA'), 'STRLQSJSWSEXRRPRLS')

    def test_encrypt_vigenre_4(self):
        self.assertEqual(encrypt_vigenere('helloworld', 'mja'), 'tnlxxwaalp')


    def test_decrypt_vigenre_1(self):
        self.assertEqual(decrypt_vigenere('slckbw', 'dnj'), 'python')

    def test_decrypt_vigenre_2(self):
        self.assertEqual(decrypt_vigenere('STRLQSJSWSEXRRPRLS', 'MMJRNNA'), 'GHIUDFJGKJNKERDFCB')

    def test_decrypt_vigenre_3(self):
        self.assertEqual(decrypt_vigenere('tnlxxwaalp', 'mja'), 'helloworld')

    def test_decrypt_vigenre_4(self):
        self.assertEqual(decrypt_vigenere('zmovsdnq', 'hhem'), 'sfkjlwje')
