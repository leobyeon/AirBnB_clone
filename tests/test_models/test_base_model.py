#!/usr/bin/python3
"""Unit test for class BaseModel"""
import unittest
from models.base_model import BaseModel
import sys, os, pep8


class TesetBaseModel(unittest.TestCase):
    """Tests for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        my_model1 = BaseModel()
        my_model1.name = "hello"
        my_model1.number = 9
        my_model2 = BaseModel()
        my_model2.name = "goodbye"
        my_model2.number = 19

    def tearDown(self):
        """tear down test set up"""
        all_ob = storage.all()
        all_ob.clear()
        storage.all()

    def test_init(self):
        """test __init__"""
        self.assertEqual(type(my_model1.name), str)
        self.assertEqual(my_model1.name, "hello")
        self.assertEqual(type(my_model1.number), int)
        self.assertEqual(my_model1.number, 9)

    def test_str(self):
        """test __srt__"""
        pass
    def test_save(self):
        """test save"""
        pass

    def test_to_dict(self):
        """test to_dict"""
        pass

    
        