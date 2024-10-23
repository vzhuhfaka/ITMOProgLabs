import unittest
from src.lab3.sudoku import group, get_row, get_col, get_block, find_empty_positions, find_possible_values, read_sudoku


class SudokuTestCase(unittest.TestCase):

    def test_sudoku_group(self):
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 4), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    def test_sudoku_get_row(self):
        self.assertEqual(get_row([['4', '2', '.'], ['.', '5', '1'], ['4', '.', '.']], (0, 0)), ['4', '2', '.'])

    def test_sudoku_get_col(self):
        self.assertEqual(get_col([['4', '2', '.'], ['.', '5', '1'], ['4', '.', '.']], (0, 0)), ['4', '.', '4'])

    def test_sudoku_get_block(self):
        self.assertEqual(get_block([['4', '2', '.'], ['.', '5', '1'], ['4', '.', '.']], (0, 0)), ['4', '2', '.', '.', '5', '1', '4', '.', '.'])

    def test_sudoku_find_empty_positions(self):
        self.assertEqual(find_empty_positions([['5', '5', '1'], ['.', '4', '2'], ['2', '.', '2']]), (1, 0))

    def test_sudoku_find_possible_values(self):
        self.assertEqual(find_possible_values(read_sudoku('src/lab3/puzzle1.txt'), (1, 2)), {'2', '4', '7'})