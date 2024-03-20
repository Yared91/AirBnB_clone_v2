#!/usr/bin/python3
"""tests State """
import unittest
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel
from models.state import State
import os


class test_state(unittest.TestCase):
    """tests the state class"""

    @classmethod
    def setUp(cls):
        """ setting up class for State"""
        cls.state = State()
        cls.state.name = "California"

    @classmethod
    def teardown(cls):
        """deletes setup"""
        del cls.state

    def tearDown(self):
        """ tests the tear down method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_state_doc(self):
        """tests docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_state_attribute(self):
        """tests attributes"""
        attributes = ['id', 'created_at', 'updated_at', 'name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.state, attribute))

    def test_state_subclass(self):
        """tests the subclass method"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_user_save(self):
        """tests the save method"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_user_to_dict(self):
        """tests to_dict method"""
        self.assertEqual('to_dict' in dir(self.state), True)

    def test_user_type(self):
        """tests the attribute type"""
        attr_type = {"name": str}
        for attribute, data_type in attr_type.items():
            self.assertEqual(type(getattr(self.state, attribute)), data_type)


if __name__ == "__main__":
    unittest.main()
