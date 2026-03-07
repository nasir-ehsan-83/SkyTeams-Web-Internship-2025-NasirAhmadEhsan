import unittest

from data_structure_algorithm.algorithm.week4.question16 import multiply_matrix
from data_structure_algorithm.algorithm.week4.question17 import abbreviate_sentence
from data_structure_algorithm.algorithm.week4.question18 import Stack
from data_structure_algorithm.algorithm.week4.question19 import QueueUsingStacks
from data_structure_algorithm.algorithm.week4.question20 import is_balanced
from data_structure_algorithm.algorithm.week4.question21 import longest_palindrome
from data_structure_algorithm.algorithm.week4.question22 import merge_intervals
from data_structure_algorithm.algorithm.week4.question23 import top_k_frequent
from data_structure_algorithm.algorithm.week4.question24 import kth_largest
from data_structure_algorithm.algorithm.week4.question25 import set_zeroes

class TestWeek4Part2(unittest.TestCase):
    def test_cases(self):
        A = [[1,2],[3,4]]
        B = [[5,6],[7,8]]
        self.assertEqual(multiply_matrix(A,B), [[19,22],[43,50]])
        self.assertEqual(multiply_matrix([[1]], [[2]]), [[2]])
        self.assertIsNone(multiply_matrix([[1,2]], [[1,2]]))

    def test_cases(self):
        self.assertEqual(abbreviate_sentence("I am learning JavaScript"), "I a l J")
        self.assertEqual(abbreviate_sentence("Hello World"), "H W")
        self.assertEqual(abbreviate_sentence(""), "")

    def test_cases(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.peek(), 30)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.size(), 2)
        self.assertFalse(stack.is_empty())

    def test_cases(self):
        q = QueueUsingStacks()
        self.assertTrue(q.empty())
        q.push(10)
        q.push(20)
        self.assertFalse(q.empty())
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.pop(), 10)
        self.assertEqual(q.pop(), 20)
        self.assertTrue(q.empty())

    def test_cases(self):
        self.assertTrue(is_balanced("()[]{}"))
        self.assertFalse(is_balanced("(]"))
        self.assertTrue(is_balanced("{[()]}"))
        self.assertFalse(is_balanced("((("))

    def test_cases(self):
        self.assertIn(longest_palindrome("babad"), ["bab","aba"])
        self.assertEqual(longest_palindrome("cbbd"), "bb")
        self.assertEqual(longest_palindrome("a"), "a")
        self.assertEqual(longest_palindrome(""), "")

    def test_cases(self):
        self.assertEqual(merge_intervals([[1,3],[2,6],[8,10]]), [[1,6],[8,10]])
        self.assertEqual(merge_intervals([[1,4],[4,5]]), [[1,5]])
        self.assertEqual(merge_intervals([]), [])

    def test_cases(self):
        self.assertEqual(top_k_frequent([1,1,1,2,2,3],2), [1,2])
        self.assertEqual(top_k_frequent([4,4,4,6,6,7],1), [4])
        self.assertEqual(top_k_frequent([],1), [])

    def test_cases(self):
        self.assertEqual(kth_largest([3,2,1,5,6,4], 2), 5)
        self.assertEqual(kth_largest([7,10,4,3,20,15], 3), 10)
        self.assertEqual(kth_largest([1,2,3], 1), 3)

    def test_cases(self):
        mat = [[1,1,1],[1,0,1],[1,1,1]]
        self.assertEqual(set_zeroes(mat), [[1,0,1],[0,0,0],[1,0,1]])
        self.assertEqual(set_zeroes([[0,1],[1,1]]), [[0,0],[0,1]])
        self.assertEqual(set_zeroes([]), [])


if __name__ == "__main__":
	unittest.main()