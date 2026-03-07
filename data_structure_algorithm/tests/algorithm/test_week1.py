import unittest

from data_structure_algorithm.algorithm.week1.question1 import add_numbers
from data_structure_algorithm.algorithm.week1.question2 import is_even
from data_structure_algorithm.algorithm.week1.question3 import reverse_string
from data_structure_algorithm.algorithm.week1.question4 import swap
from data_structure_algorithm.algorithm.week1.question5 import max_of_three
from data_structure_algorithm.algorithm.week1.question6 import min_of_three
from data_structure_algorithm.algorithm.week1.question7 import rectangle_area_perimeter
from data_structure_algorithm.algorithm.week1.question8 import celcius_to_fahrenhait
from data_structure_algorithm.algorithm.week1.question9 import simple_interest, compound_interest
from data_structure_algorithm.algorithm.week1.question10 import seconds_to_hms


class TestWeek1(unittest.TestCase):
	# test add_numbers() 
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
	
	# test is_even()
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
        self.assertTrue(is_even(0))
        
    # test reverse_string()
    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
	
	# test swap()
    def test_swap(self):
        a, b = swap(5, 10)
        self.assertEqual((a, b), (10, 5))
        a, b = swap(-1, 1)
        self.assertEqual((a, b), (1, -1))
        
    # test max_of_three()
    def test_max_of_three(self):
        self.assertEqual(max_of_three(3, 9, 5), 9)
        self.assertEqual(max_of_three(0, -1, -2), 0)
	
	# test min_of_three()
    def test_min_of_three(self):
        self.assertEqual(min_of_three(3, 9, 5), 3)
        self.assertEqual(min_of_three(0, -1, -2), -2)
	
	# test rectangle_area_perimeter()
    def test_rectangle_area_perimeter(self):
        area, perimeter = rectangle_area_perimeter(4, 6)
        self.assertEqual((area, perimeter), (24, 20))
        area, perimeter = rectangle_area_perimeter(0, 5)
        self.assertEqual((area, perimeter), (0, 10))
	
	# test celcius_to_fahrenhait()
    def test_celcius_to_fahrenhait(self):
        self.assertEqual(celcius_to_fahrenhait(25), 77)
    
    # test fahrenhait_to_celcius()
    def test_fahrenhait_to_celcius(self):
        self.assertEqual(celcius_to_fahrenhait(77), 25)

	# test simple_interest() and compund_interest()
    def test_interest(self):
        self.assertEqual(simple_interest(1000, 5, 2), 100)
        self.assertEqual(compound_interest(1000, 5, 2), 102)

	# test seconds_to_hms()
    def test_seconds_to_hms(self):
        self.assertEqual(seconds_to_hms(3665), (1, 1, 5))
        self.assertEqual(seconds_to_hms(59), (0, 0, 59))


if __name__ == "__main__":
    unittest.main()
