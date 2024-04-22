#!/usr/bin/python3
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle


"""Test rectangle"""

class TestRectangleFunction(unittest.TestCase):
    """TestRectangle: function to test the rectangle function

    Args:
        unittest (argument): class argument
    """

    def test_init_with_id_2(self):
        """test rectangle class where id is provided"""
        obj  = Rectangle(10, 2, 0, 0, 12)
        obj1 = Rectangle(10, 5, 0, 2, 3)
        self.assertEqual(obj.id, 12)
        self.assertEqual(obj1.id, 3)

    def test_init_without_id_2(self):
        """test rectangle calss whrer id is not provided"""
        obj1 = Rectangle(10, 2)
        obj2 = Rectangle(2, 10)
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
    
    def test_all_attrubutes_2(self):
        """test all attributes of the class rectangle"""
        obj1 = Rectangle(5, 5, 2, 2, 1)
        self.assertEqual(obj1.width, 5)
        self.assertEqual(obj1.height, 5)
        self.assertEqual(obj1.x, 2)
        self.assertEqual(obj1.y, 2)

    def test_type_error_3(self):
        """test all type errors"""
        with self.assertRaises(TypeError):
            obj1 = Rectangle("width", 2, 5, 2, 6)
        
        with self.assertRaises(TypeError):
            obj1 = Rectangle(2, "height", 3, 5, 5)

        with self.assertRaises(TypeError):
            obj1 = Rectangle(2, 5, "x", 5)

        with self.assertRaises(TypeError):
            obj1 = Rectangle(2, 5, 1, "y", 2)

    def test_string_representation(self):
        """Test string representation of the rectangle"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        
        expected_r1_str = "[Rectangle] (12) 2/1 - 4/6"
        expected_r2_str = "[Rectangle] (3) 1/0 - 5/5"

        self.assertEqual(str(r1), expected_r1_str)
        self.assertEqual(str(r2), expected_r2_str)
    
    def test_dictionnary_representation_13(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(1, 1, 0, 0, 2)

        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()

        expected_r1_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        expected_r2_dict = {'id': 2, 'width': 1, 'height': 1, 'x': 0, 'y': 0}

        self.assertDictEqual(r1_dict, expected_r1_dict)
        self.assertDictEqual(r2_dict, expected_r2_dict)
      
    def test_update_function_8(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(98)
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(33, 2)
        r2.update(33, 2, 5, 7, 5)

        self.assertEqual(r1.id, 98)
        self.assertEqual(r2.id, 33)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 5)


    def test_value_error_3(self):
        """test type and value errors"""
        with self.assertRaises(ValueError):
            obj1 = Rectangle(-1, -2, -3, - 3, 4)
        
        with self.assertRaises(ValueError):
            obj1 = Rectangle(1, 2, -3, 4, 5)
        
        with self.assertRaises(TypeError):
            obj1 = Rectangle(4.1, 1, 3, 6, 7)
        
        with self.assertRaises(TypeError):
            obj1 = Rectangle(1, 2.5, 1, 5, 5)
        
        with self.assertRaises(TypeError):
            obj1 = Rectangle(1, 3, 3.5, 6, 8)
        
        with self.assertRaises(TypeError):
            obj1 = Rectangle(1, 2, 3, 4.5, 5)

    def test_area_case_4(self):
        """test area of the rectangle"""
        r1 = Rectangle(3, 2, 2, 4, 6)
        r2 = Rectangle(33243424242, 3, 1, 5, 6)
        self.assertEqual(r2.area(), 99730272726)
        self.assertEqual(r1.area(), 6)

        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2, 5, 6, 3)

        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -3, 5)

        with self.assertRaises(TypeError):
            r2 = Rectangle(1, 2.4, 5, 5, 6)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1)


        with self.assertRaises(TypeError):
            r1 = Rectangle()

class Output_testing(unittest.TestCase):
    """Test the output produced by display function"""
    def setUp(self):
        """setting up the the file to capture the output"""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """setting up the file"""
        sys.stdout = sys.__stdout__    

    def test_display_function_5(self):
        """test display function"""
        my_rectangle = Rectangle(2, 5, 3, 5, 6)
        my_rectangle.display()
    
        expected_output = "\n\n\n\n\n   ##\n   ##\n   ##\n   ##\n   ##\n"
        captured_output = self.held_output.getvalue()

        self.assertEqual(captured_output, expected_output)


