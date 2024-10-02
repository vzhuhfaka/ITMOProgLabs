import unittest
from src.lab3.sudoku import group, get_row, get_col, get_block

class SudokuTestCase(unittest.TestCase):

    def test_sudoku_group(self):
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 4), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    def test_sudoku_get_row(self):
        self.assertEqual(get_row([['4', '2', '.'], ['.', '5', '1'], ['4', '.', '.']], (0, 0)), ['4', '2', '.'])

    def test_sudoku_get_col(self):
        self.assertEqual(get_col([['4', '2', '.'], ['.', '5', '1'], ['4', '.', '.']], (0, 0)), ['4', '.', '4'])

    def test_sudoku_get_block(self):
        self.assertEqual(get_block([['4', '2', '.'], ['.', '5', '1'], ['4', '.', '.']], (0, 0)), ['4', '2', '.', '.', '5', '1', '4', '.', '.'])
