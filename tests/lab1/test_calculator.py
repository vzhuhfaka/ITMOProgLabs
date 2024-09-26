import unittest
from src.lab1.calculator import calculator

class CalculatorTestCase(unittest.TestCase):

    def test_calculator(self):
        self.assertEqual(calculator(1, 3), 4)
