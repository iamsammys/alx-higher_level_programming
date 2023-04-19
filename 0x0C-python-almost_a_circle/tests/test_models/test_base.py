#!/usr/bin/python3

"""module to test the Base class
"""

from models.base import Base
import inspect
import json
import unittest


class TestBase(unittest.TestCase):
    """Test class for unittest
    """

    @classmethod
    def setUpClass(cls):
        """creates instances and variables
        """
        cls.my_inst = Base()
        cls.j_string = json.dumps([{"key": "first_key"},
                                    {"key_2": "second_key"}])
        cls.dict_lst = [{"key": "first_key"}, {"key_2": "second_key"}]
        cls.functions = inspect.getmembers(Base, predicate=inspect.ismethod)
    
    def test_cls_doc(self):
        """tests class documentation
        """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_f_doc(self):
        """tests the function documentation
        """
        for f_name, function in self.functions:
            self.assertTrue(len(function.__doc__) > 0)
    def test_Base_id(self):
        """tests the id attribute
        """
        self.assertTrue(self.my_inst.id == 1)
        inst = Base(4)
        self.assertEqual(inst.id, 4)
        inst = Base(None)
        self.assertEqual(inst.id, 2)

    def test_to_json_string(self):
        """tests to_json method
        """
        json_string = Base.to_json_string(self.dict_lst)
        self.assertEqual(json_string, self.j_string)
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual("[]", Base.to_json_string(None))

    def test_from_json_string(self):
        """tests from_json_string function
        """
        self.assertEqual(self.dict_lst, Base.from_json_string(self.j_string))
        self.assertEqual([], Base.from_json_string(None))
        self.assertEqual([], Base.from_json_string("[]"))
