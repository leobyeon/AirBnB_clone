#!/usr/bin/python3
"""Unit test for class Review"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from unittest.mock import create_autospec
import sys
import os
import pep8
from console import HBNBCommand


class TestReview(unittest.TestCase):
    """Tests for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model1 = Review()
        self.my_model1.place_id = "Ca"
        self.my_model1.user_id = "Me"
        self.my_model1.text = "Hello you"
        self.my_model2 = Review()
        self.my_model2.name = "goodbye"
        self.my_model2.number = 19
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_review(self):
        """test for review"""
        self.assertEqual(self.my_model1.place_id, "Ca")
        self.assertEqual(self.my_model1.user_id, "Me")
        self.assertEqual(self.my_model1.text, "Hello you")

if __name__ == '__main__':
    unittest.main()
