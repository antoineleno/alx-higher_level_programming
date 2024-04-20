#!/usr/bin/python3
import unittest
from io import StringIO
import sys
from models.square import Square


"""Test rectangle"""
class TestSquareFunction(unittest.TestCase):
    """Class to test function"""
    def test_case_if_Square_has_access_to_rectangle_method(self):
        """test method and attribures accesss"""
        obj  = Square(10, 2, 0, 0)
        obj1 = Square(10, 5, 0, 2)
        self.assertEqual(obj.id, 0)
        self.assertEqual(obj1.id, 2)
        self.assertEqual(obj1.area(), 100)
        self.assert_(obj.area(), 100)

    def test_case_without_id_10(self):
        """test class variable accesss"""
        obj1 = Square(1, 5, 6)
        obj2 = Square(11, 5, 6)

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_all_attrubutes_10(self):
        """test all attributes of the class rectangle"""
        obj1 = Square(5, 5, 2, 2)
        self.assertEqual(obj1.size, 5)
        self.assertEqual(obj1.id, 2)
        self.assertEqual(obj1.x, 5)
        self.assertEqual(obj1.y, 2)
        
    def test_type_error_3(self):
        """test all type errors"""
        with self.assertRaises(TypeError):
            obj1 = Square("size", 2, 5, 2)

        with self.assertRaises(TypeError):
            obj1 = Square(2, 5, "x", 5)

        with self.assertRaises(TypeError):
            obj1 = Square(2, 1, "y", 2)

    def test_update_function_8(self):
        """test update method"""
        s1 = Square(10, 10, 10, 10)
        s1.update(98)
        s2 = Square(10, 5, 10, 10)
        s2.update(33, 2)
        s2.update(33, 2, 5, 7)

        self.assertEqual(s1.id, 98)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 5)
        self.assertEqual(s2.y, 7)

    def test_string_representation(self):
        """Test string representation of the rectangle"""
        s1 = Square(4, 6, 2, 12)
        s2 = Square(5, 5, 1, 3)
        
        expected_r1_str = "[Square] (12) 6/2 - 4"
        expected_r2_str = "[Square] (3) 5/1 - 5"

        self.assertEqual(str(s1), expected_r1_str)
        self.assertEqual(str(s2), expected_r2_str)

    def test_dictionnary_representation_13(self):
        s1 = Square(10, 2, 1, 9)
        s2 = Square(1, 1, 0, 0)

        s1_dict = s1.to_dictionary()
        s2_dict = s2.to_dictionary()

        expected_r1_dict = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        expected_r2_dict = {'id': 0, 'size': 1, 'x': 1, 'y': 0}
    
        self.assertDictEqual(s1_dict, expected_r1_dict)
        self.assertDictEqual(s2_dict, expected_r2_dict)