import unittest

from data_structure_algorithm.algorithm.week3.question16 import fibonacci
from data_structure_algorithm.algorithm.week3.question17 import right_triangle
from data_structure_algorithm.algorithm.week3.question18 import right_aligned_triangle
from data_structure_algorithm.algorithm.week3.question19 import pyramid
from data_structure_algorithm.algorithm.week3.question20 import bmi_calculator
from data_structure_algorithm.algorithm.week3.question21 import password_strength
from data_structure_algorithm.algorithm.week3.question22 import collatz_sequence
from data_structure_algorithm.algorithm.week3.question23 import factorial_recursive
from data_structure_algorithm.algorithm.week3.question24 import pascal_triangle
from data_structure_algorithm.algorithm.week3.question25 import guess_number_game
from data_structure_algorithm.algorithm.week3.question26 import decimal_to_binary
from data_structure_algorithm.algorithm.week3.question27 import unique_elements
from data_structure_algorithm.algorithm.week3.question28 import remove_duplicates
from data_structure_algorithm.algorithm.week3.question29 import arrays_equal
from data_structure_algorithm.algorithm.week3.question30 import find_missing_number

class TestWeek3Part2(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(7), [0,1,1,2,3,5,8])
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])

    def test_right_triangle(self):
        self.assertEqual(right_triangle(4), ['*','**','***','****'])

    def test_right_aligned_triangle(self):
        self.assertEqual(right_aligned_triangle(4), ['   *','  **',' ***','****'])

    def test_pyramid(self):
        self.assertEqual(pyramid(5), ['    *','   ***','  *****',' *******','*********'])

    def test_bmi_calculator(self):
        self.assertEqual(bmi_calculator(70,1.75), (22.86,'Normal weight'))
        self.assertEqual(bmi_calculator(50,1.75), (16.33,'Underweight'))

    def test_password_strength(self):
        self.assertEqual(password_strength("MyPass123"), "Strong")
        self.assertEqual(password_strength("pass"), "Weak")
        self.assertEqual(password_strength("PASSWORD123"), "Weak")

    def test_collatz_sequence(self):
        self.assertEqual(collatz_sequence(6), ([6,3,10,5,16,8,4,2,1], 8))

    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(0), 1)

    def test_pascal_triangle(self):
        self.assertEqual(pascal_triangle(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

    def test_guess_number_game(self):
        self.assertEqual(guess_number_game(50,50), "Correct")
        self.assertEqual(guess_number_game(50,40), "Too Low")
        self.assertEqual(guess_number_game(50,60), "Too High")

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(0), "0")

class TestQuestion27(unittest.TestCase):
    def test_unique_elements(self):
        self.assertEqual(unique_elements([1,2,2,3,4,4,5]), [1,2,3,4,5])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([3,1,3,5,1]), [3,1,5])

    def test_arrays_equal(self):
        self.assertTrue(arrays_equal([1,2,3],[1,2,3]))
        self.assertFalse(arrays_equal([1,2,3],[1,3,2]))

    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([1,2,4,5],5),3)
        self.assertEqual(find_missing_number([1,2,3,4,5],5),0)

if __name__ == "__main__":
	unittest.main()