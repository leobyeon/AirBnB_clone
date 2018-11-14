#!/usr/bin/python3
"""Unit test for class BaseModel"""
import unittest
from models.base_model import BaseModel
from unittest.mock import create_autospec
import sys
import os
import pep8
from console import HBNBCommand
from models import storage
import tests


class TestBaseModel(unittest.TestCase):
    """Tests for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model1 = BaseModel()
        self.my_model1.name = "hello"
        self.my_model1.number = 9
        self.my_model2 = BaseModel()
        self.my_model2.name = "goodbye"
        self.my_model2.number = 19
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """:return: last 'n' output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(
            lambda c: c[0][0], self.mock_stdout.write.call_args_list[-nr:]))

    def tearDown(self):
        """tear down test set up"""
        self.all_ob = storage.all()
        self.all_ob.clear()
        storage.save()

    def test_init(self):
        """test __init__"""
        self.assertEqual(type(self.my_model1.name), str)
        self.assertEqual(self.my_model1.name, "hello")
        self.assertEqual(type(self.my_model1.number), int)
        self.assertEqual(self.my_model1.number, 9)

    def test_quit(self):
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))
        self.assertTrue(cli.onecmd("EOF"))

    def test_str(self):
        """test __srt__"""
        pass

    def test_save(self):
        """test save"""
        pass

    def test_to_dict(self):
        """test to_dict"""
        pass
if __name__ == '__main__':
    unittest.main()