import unittest
from src.lab3.sudoku import group

class SudokuTestCase(unittest.TestCase):

    def test_sudoku_group(self):
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 4), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

