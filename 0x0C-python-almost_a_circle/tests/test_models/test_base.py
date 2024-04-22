#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys
import json
import os


"""TestBase"""
class TestBase(unittest.TestCase):
    """Test Base

    Args:
        unittest (_type_): test case
    """

    def test_init_without_id(self):
        """test_init_without_id"""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 3)
        self.assertEqual(obj2.id, 4)
        self.assertEqual(obj3.id, 5)
        self.assertEqual(obj2.id - obj1.id, 1)

    def test_init_with_id(self):
        """test base case where id is provided"""
        obj1 = Base(10)
        obj2 = Base(-1)
        obj3 = Base(0)
        self.assertEqual(obj1.id, 10)
        self.assertEqual(obj2.id, -1)
        self.assertEqual(obj3.id, 0)

    def test_to_json_string(self):
        """test json string representation"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        parsed_json = json.loads(json_string)

        expected_json = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        self.assertEqual(parsed_json, expected_json)

        json_string_empty = Base.to_json_string([])
        parsed_json_empty = json.loads(json_string_empty)
        self.assertEqual(parsed_json_empty, [])

        json_string_none = Base.to_json_string(None)
        parsed_json_none = json.loads(json_string_none)
        self.assertEqual(parsed_json_none, [])

    def test_save_to_file(self):
        """test save to file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertTrue(content.startswith("[{"))
        self.assertTrue(content.endswith("}]"))
        self.assertIn('"width": 10, "height": 7, "x": 2, "y": 8', content)
        self.assertIn('"width": 2, "height": 4, "x": 0, "y": 0', content)

        os.remove("Rectangle.json")

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()

        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsNot(r1, r2)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])

        rectangles_loaded = Rectangle.load_from_file()

        for rect in rectangles_loaded:
            self.assertIsInstance(rect, Rectangle)

        self.assertEqual(rectangles_loaded[0].width, r1.width)
        self.assertEqual(rectangles_loaded[0].height, r1.height)
        self.assertEqual(rectangles_loaded[0].x, r1.x)
        self.assertEqual(rectangles_loaded[0].y, r1.y)

        self.assertEqual(rectangles_loaded[1].width, r2.width)
        self.assertEqual(rectangles_loaded[1].height, r2.height)
        self.assertEqual(rectangles_loaded[1].x, r2.x)
        self.assertEqual(rectangles_loaded[1].y, r2.y)