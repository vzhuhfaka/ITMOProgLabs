import string
import unittest
import random

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

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))
