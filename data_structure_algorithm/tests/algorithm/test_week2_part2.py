import unittest

from data_structure_algorithm.algorithm.week2.question16 import numbers_1_to_100
from data_structure_algorithm.algorithm.week2.question17 import sum_natural
from data_structure_algorithm.algorithm.week2.question18 import multiplication_table
from data_structure_algorithm.algorithm.week2.question19 import reverse_number
from data_structure_algorithm.algorithm.week2.question20 import count_digits
from data_structure_algorithm.algorithm.week2.question21 import sum_of_digits
from data_structure_algorithm.algorithm.week2.question22 import even_numbers
from data_structure_algorithm.algorithm.week2.question23 import fibonacci
from data_structure_algorithm.algorithm.week2.question24 import gcd
from data_structure_algorithm.algorithm.week2.question25 import lcm

class TestWeek2Part2(unittest.TestCase):
	# test numbers_1_to_100()
    def test_numbers_1_to_100(self):
        result = numbers_1_to_100()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[-1], 100)
        self.assertEqual(len(result), 100)

	# test sum_natural()
    def test_sum_natural(self):
        self.assertEqual(sum_natural(5), 15)
        self.assertEqual(sum_natural(10), 55)

	# test multipication_table()
    def test_multiplication_table(self):
        table = multiplication_table(5,3)
        self.assertEqual(table, [(5,1,5),(5,2,10),(5,3,15)])
	
	# test reverse_number()
    def test_reverse_number(self):
        self.assertEqual(reverse_number(1234), 4321)
        self.assertEqual(reverse_number(100), 1)

	# test count_digits()
    def test_count_digits(self):
        self.assertEqual(count_digits(786), 3)
        self.assertEqual(count_digits(0), 0)
	
	# test sum_of_digits()
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(786), 21)

	# test even_numbers() return a list of even numbers between two number
    def test_even_numbers(self):
        self.assertEqual(even_numbers(1,10), [2,4,6,8,10])
        self.assertEqual(even_numbers(3,7), [4,6])
	
	# test fibonacci()
    def test_fibonacci(self):
        self.assertEqual(fibonacci(7), [0,1,1,2,3,5,8])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(0), [])

	# test gcd()
    def test_gcd(self):
        self.assertEqual(gcd(12,18), 6)
        self.assertEqual(gcd(7,5), 1)
	
	# test ldm()
    def test_lcm(self):
        self.assertEqual(lcm(12,18), 36)
        self.assertEqual(lcm(7,5), 35)

if __name__ == "__main__":
	unittest.main()