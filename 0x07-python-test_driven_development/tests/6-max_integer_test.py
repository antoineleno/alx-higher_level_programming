#!/usr/bin/python3
import unittest
# Assuming '6-max_integer' is the correct module name and path
max_integer = __import__('6-max_integer').max_integer


"""Class: Class for testing"""
class TestFunctionMaxInteger(unittest.TestCase):
    """Mix test all numbers are positive"""
    def test_max_integer(self):
        self.assertEqual(max_integer([85, 0, 44, 450]), 450)

    def test_list_same_elements(self):
        """test case where all elements are same"""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_list_none(self):
        """case where list is none"""
        self.assertEqual(max_integer([]), None)

    def test_list_all_negative(self):
        """test case where all elements are positive"""
        self.assertEqual(max_integer([-10, -5, -15]), -5)

    def test_positives_and_negatives(self):
        """Unittest for max_integer([positive and negative value])"""
        self.assertEqual(
            max_integer([-23, 558, 91, -24, 10, 89, 98, 581, -256, -512]), 581)

    def test_float(self):
        """test case where elements are float"""
        self.assertEqual(max_integer([-23.36, 91.21, -24.25, 10.3, 8.9, 19.8, -25.6, -51.2]), 91.21)

    def test_one_not_int(self):
        """an element not an int or float"""
        with self.assertRaises(TypeError):
            max_integer([1, "no"])


if __name__ == '__main__':
    unittest.main()
