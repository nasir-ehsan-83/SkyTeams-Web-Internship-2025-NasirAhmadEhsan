import unittest

from data_structure_algorithm.algorithm.week3.question1 import count_vowels
from data_structure_algorithm.algorithm.week3.question2 import reverse_number
from data_structure_algorithm.algorithm.week3.question3 import sum_of_digits
from data_structure_algorithm.algorithm.week3.question4 import factors
from data_structure_algorithm.algorithm.week3.question5 import largest
from data_structure_algorithm.algorithm.week3.question6 import smallest
from data_structure_algorithm.algorithm.week3.question7 import sum_array
from data_structure_algorithm.algorithm.week3.question8 import contains
from data_structure_algorithm.algorithm.week3.question9 import count_occurrences
from data_structure_algorithm.algorithm.week3.question10 import is_prime
from data_structure_algorithm.algorithm.week3.question11 import primes_up_to
from data_structure_algorithm.algorithm.week3.question12 import is_palindrome
from data_structure_algorithm.algorithm.week3.question13 import power
from data_structure_algorithm.algorithm.week3.question14 import factorial
from data_structure_algorithm.algorithm.week3.question15 import is_armstrong

class TestWeek3Part1(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("SkyTeams Internship"), 6)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_reverse_number(self):
        self.assertEqual(reverse_number(1234), 4321)
        self.assertEqual(reverse_number(100), 1)
        self.assertEqual(reverse_number(0), 0)

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(sum_of_digits(0), 0)

    def test_factors(self):
        self.assertEqual(factors(12), [1,2,3,4,6,12])
        self.assertEqual(factors(7), [1,7])

    def test_largest(self):
        self.assertEqual(largest([2,8,5,3,9]), 9)
        self.assertEqual(largest([]), None)

    def test_smallest(self):
        self.assertEqual(smallest([4,7,1,9,2]), 1)
        self.assertEqual(smallest([]), None)

    def test_sum_array(self):
        self.assertEqual(sum_array([1,2,3,4,5]), 15)
        self.assertEqual(sum_array([]), 0)

    def test_contains(self):
        self.assertTrue(contains([3,6,9,12], 6))
        self.assertFalse(contains([3,6,9,12], 7))

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([2,3,2,5,2], 2), 3)
        self.assertEqual(count_occurrences([1,2,3], 4), 0)

    def test_is_prime(self):
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(20))
        self.assertFalse(is_prime(1))

    def test_primes_up_to(self):
        self.assertEqual(primes_up_to(10), [2,3,5,7])
        self.assertEqual(primes_up_to(1), [])

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(123))

    def test_power(self):
        self.assertEqual(power(2,5), 32)
        self.assertEqual(power(3,0), 1)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_is_armstrong(self):
        self.assertTrue(is_armstrong(153))
        self.assertFalse(is_armstrong(123))


if __name__ == "__main__":
	unittest.main()