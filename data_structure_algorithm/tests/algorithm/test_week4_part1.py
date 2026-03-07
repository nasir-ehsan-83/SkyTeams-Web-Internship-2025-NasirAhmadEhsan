import unittest

from data_structure_algorithm.algorithm.week4.question1 import second_largest
from data_structure_algorithm.algorithm.week4.question2 import merge_sorted_arrays
from data_structure_algorithm.algorithm.week4.question3 import rotate_right
from data_structure_algorithm.algorithm.week4.question4 import intersection
from data_structure_algorithm.algorithm.week4.question5 import rearrange_even_odd
from data_structure_algorithm.algorithm.week4.question6 import binary_search
from data_structure_algorithm.algorithm.week4.question7 import rock_paper_scissors
from data_structure_algorithm.algorithm.week4.question8 import ATM
from data_structure_algorithm.algorithm.week4.question9 import compress_string
from data_structure_algorithm.algorithm.week4.question10 import is_unique
from data_structure_algorithm.algorithm.week4.question11 import is_rotation
from data_structure_algorithm.algorithm.week4.question12 import char_frequency
from data_structure_algorithm.algorithm.week4.question13 import pattern_match
from data_structure_algorithm.algorithm.week4.question14 import string_permutations
from data_structure_algorithm.algorithm.week4.question15 import max_subarray_sum


class TestWeek4Part1(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(second_largest([10, 20, 4, 45, 99]), 45)
        self.assertEqual(second_largest([1,2]), 1)
        self.assertEqual(second_largest([5,5,5]), None)
        self.assertEqual(second_largest([1]), None)

    def test_cases(self):
        self.assertEqual(merge_sorted_arrays([1,3,5],[2,4,6]), [1,2,3,4,5,6])
        self.assertEqual(merge_sorted_arrays([], [1,2]), [1,2])
        self.assertEqual(merge_sorted_arrays([1,2], []), [1,2])
        self.assertEqual(merge_sorted_arrays([], []), [])

    def test_cases(self):
        self.assertEqual(rotate_right([1,2,3,4,5], 2), [4,5,1,2,3])
        self.assertEqual(rotate_right([1,2,3], 3), [1,2,3])
        self.assertEqual(rotate_right([], 5), [])
        self.assertEqual(rotate_right([1], 10), [1])

    def test_cases(self):
        self.assertEqual(intersection([1,2,3,4],[3,4,5,6]), [3,4])
        self.assertEqual(intersection([1,1,2],[1,2]), [1,2])
        self.assertEqual(intersection([], [1,2]), [])
        self.assertEqual(intersection([1,2], []), [])

    def test_cases(self):
        self.assertEqual(rearrange_even_odd([1,2,3,4,5,6]), [2,4,6,1,3,5])
        self.assertEqual(rearrange_even_odd([2,4,6]), [2,4,6])
        self.assertEqual(rearrange_even_odd([1,3,5]), [1,3,5])
        self.assertEqual(rearrange_even_odd([]), [])

    def test_cases(self):
        self.assertEqual(binary_search([1,3,5,7,9], 7), 3)
        self.assertEqual(binary_search([1,3,5,7,9], 2), -1)
        self.assertEqual(binary_search([], 1), -1)
        self.assertEqual(binary_search([1], 1), 0)

    def test_cases(self):
        # Since random is involved, just test if output is one of the expected
        for choice in ["rock","paper","scissors"]:
            result = rock_paper_scissors(choice)
            self.assertIn(result, ["Draw","Player wins","Computer wins"])

    def test_cases(self):
        atm = ATM()
        self.assertEqual(atm.deposit(100), "100 deposited successfully")
        self.assertEqual(atm.withdraw(50), "50 withdrawn successfully")
        self.assertEqual(atm.get_balance(), 50)
        self.assertEqual(atm.withdraw(100), "Insufficient balance")

    def test_cases(self):
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(compress_string(""), "")
        self.assertEqual(compress_string("abc"), "a1b1c1")

    def test_cases(self):
        self.assertTrue(is_unique("abc"))
        self.assertFalse(is_unique("hello"))
        self.assertTrue(is_unique(""))

    def test_cases(self):
        self.assertTrue(is_rotation("waterbottle","erbottlewat"))
        self.assertFalse(is_rotation("abc","acb"))
        self.assertTrue(is_rotation("",""))

    def test_cases(self):
        self.assertEqual(char_frequency("banana"), {'b':1,'a':3,'n':2})
        self.assertEqual(char_frequency(""), {})
        self.assertEqual(char_frequency("aa"), {'a':2})

    def test_cases(self):
        self.assertTrue(pattern_match("abba","dog cat cat dog"))
        self.assertFalse(pattern_match("abba","dog cat cat fish"))
        self.assertFalse(pattern_match("abc","dog cat cat"))

    def test_cases(self):
        result = string_permutations("abc")
        expected = ['abc','acb','bac','bca','cab','cba']
        self.assertCountEqual(result, expected)
        self.assertEqual(string_permutations("a"), ['a'])
        self.assertEqual(string_permutations(""), [''])

    def test_cases(self):
        self.assertEqual(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(max_subarray_sum([1,2,3]), 6)
        self.assertEqual(max_subarray_sum([-1,-2,-3]), -1)
        self.assertEqual(max_subarray_sum([]), 0)

if __name__ == "__main__":
	unittest.main()