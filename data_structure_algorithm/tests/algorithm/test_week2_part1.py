import unittest

from data_structure_algorithm.algorithm.week2.question1 import swap
from data_structure_algorithm.algorithm.week2.question2 import largest_smallest
from data_structure_algorithm.algorithm.week2.question3 import rectangle_area_perimeter
from data_structure_algorithm.algorithm.week2.question4 import celsius_to_fahrenheit, fahrenheit_to_celsius
from data_structure_algorithm.algorithm.week2.question5 import simple_interest, compound_interest
from data_structure_algorithm.algorithm.week2.question6 import seconds_to_hms
from data_structure_algorithm.algorithm.week2.question7 import is_even
from data_structure_algorithm.algorithm.week2.question8 import number_type
from data_structure_algorithm.algorithm.week2.question9 import grade
from data_structure_algorithm.algorithm.week2.question10 import is_leap_year
from data_structure_algorithm.algorithm.week2.question11 import calculator
from data_structure_algorithm.algorithm.week2.question12 import traffic_light
from data_structure_algorithm.algorithm.week2.question13 import month_info
from data_structure_algorithm.algorithm.week2.question14 import letter_type
from data_structure_algorithm.algorithm.week2.question15 import triangle_type

class TestWeek2Part1(unittest.TestCase):
	# test swap()
    def test_swap(self):
        self.assertEqual(swap(5, 10), (10, 5))
        self.assertEqual(swap(0, -1), (-1, 0))
    
    # test largest_smallest()
    def test_largest_smallest(self):
        self.assertEqual(largest_smallest(3, 9, 5), (9, 3))
        self.assertEqual(largest_smallest(-1, -5, 0), (0, -5))

	# test rectangle_area_perimeter()
    def test_rectangle_area_perimeter(self):
        self.assertEqual(rectangle_area_perimeter(4, 6), (24, 20))
        self.assertEqual(rectangle_area_perimeter(0, 5), (0, 10))

	# test celcius_to_fahrenhait()
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(25), 77)
    
    # test fahrenhait_to_celcius()
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(77), 25)

	# test simple_interest() and compound_interest()
    def test_interest(self):
        self.assertEqual(simple_interest(1000, 5, 2), 100)
        self.assertEqual(compound_interest(1000, 5, 2), 102)

	# test seconds_to_hms()
    def test_seconds_to_hms(self):
        self.assertEqual(seconds_to_hms(3665), (1, 1, 5))
        self.assertEqual(seconds_to_hms(59), (0, 0, 59))

	# test is_even()
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
        self.assertTrue(is_even(0))

	# test number_type()
    def test_number_type(self):
        self.assertEqual(number_type(5), "Positive")
        self.assertEqual(number_type(-3), "Negative")
        self.assertEqual(number_type(0), "Zero")
	
	# test grade()
    def test_grade(self):
        self.assertEqual(grade(95), "A")
        self.assertEqual(grade(85), "B")
        self.assertEqual(grade(50), "F")

	# test is_leap_year()
    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2024))

	# test calculator()
    def test_calculator(self):
        self.assertEqual(calculator(5, 3, '+'), 8)
        self.assertEqual(calculator(5, 3, '-'), 2)
        self.assertEqual(calculator(5, 3, '*'), 15)
        self.assertEqual(calculator(6, 3, '/'), 2)
        self.assertIsNone(calculator(6, 0, '/'))

	# test traffic_lignt()
    def test_traffic_light(self):
        self.assertEqual(traffic_light('Red'), "Stop")
        self.assertEqual(traffic_light('Yellow'), "Ready")
        self.assertEqual(traffic_light('Green'), "Go")
        self.assertEqual(traffic_light('Blue'), "Invalid")
	
	# test month_info()
    def test_month_info(self):
        self.assertEqual(month_info(2), ("February", 28))
        self.assertEqual(month_info(4), ("April", 30))
        self.assertEqual(month_info(13), ("Invalid", 0))

	# test letter_type()
    def test_letter_type(self):
        self.assertEqual(letter_type('a'), "Vowel")
        self.assertEqual(letter_type('b'), "Consonant")
        self.assertEqual(letter_type('5'), "Digit")
        self.assertEqual(letter_type('#'), "Special")

	# test triangle_type()
    def test_triangle_type(self):
        self.assertEqual(triangle_type(3,3,3), "Equilateral")
        self.assertEqual(triangle_type(3,3,5), "Isosceles")
        self.assertEqual(triangle_type(3,4,5), "Scalene")
        self.assertEqual(triangle_type(1,2,3), "Invalid")

if __name__ == "__main__":
	unittest.main()