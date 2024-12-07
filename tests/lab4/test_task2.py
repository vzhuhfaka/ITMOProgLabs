import unittest
from src.lab4.task2.task2 import Group

class TestGroup(unittest.TestCase):
    def test_should_paste_into_groups(self):
        dict_group_ = {(0, 10): [], (11, 20): [], (21, 30): []}
        respondents_ = [('A', 10), ('B', 15), ('C', 20), ('D', 25), ('E', 30)]
        must_be_dict = {(0, 10): [('A', 10)], (11, 20): [('B', 15), ('C', 20)], (21, 30): [('D', 25), ('E', 30)]}

        obj = Group(dict_group_, respondents_)
        obj.paste_into_groups()
        self.assertEqual(dict_group_, must_be_dict)

    def test_should_sort_groups(self):
        dict_group_ = {(0, 10): [('A', 10), ('B', 15), ('C', 20)], (11, 20): [('D', 25), ('E', 30)]}
        must_be_dict = {(0, 10): [('C', 20), ('B', 15), ('A', 10)], (11, 20): [('E', 30), ('D', 25)]}

        obj = Group(dict_group_, [])
        obj.sort_dict_group()
        self.assertEqual(dict_group_, must_be_dict)

    def test_should_get_formatted_dict_group(self):
        dict_group_ = {(0, 10): [('A', 10), ('B', 15), ('C', 20)], (11, 20): [('D', 25), ('E', 30)]}
        must_be_dict = '11-20: E (30), D (25)\n0-10: C (20), B (15), A (10)\n'

        obj = Group(dict_group_, [])
        obj.sort_dict_group()
        self.assertEqual(obj.get_formatted_dict_group(), must_be_dict)
