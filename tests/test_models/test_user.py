#!/usr/bin/python3
""" unittest for User"""
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel
from models.user import User
import os
import unittest


class TestUser(unittest.TestCase):
    """tests the User class """

    @classmethod
    def setUp(cls):
        """ setting up class for user"""
        cls.user = User()
        cls.user.first_name = "Elilta"
        cls.user.last_name = "Alemu"
        cls.user.email = "eleltaalemu@gmail.com"
        cls.user.password = "Donottouchit"

    @classmethod
    def teardown(cls):
        """deletes setup"""
        del cls.user

    def tearDown(self):
        """ tests the tear down method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_user_doc(self):
        """tests docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_user_attribute(self):
        """tests attributes"""
        attributes = ['email', 'id', 'created_at', 'updated_at', 'password',
                'first_name', 'last_name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.user, attribute))

    def test_user_subclass(self):
        """tests the subclass method"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_user_save(self):
        """tests the save method"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_user_to_dict(self):
        """tests to_dict method"""
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_user_type(self):
        """tests the attribute type"""
        attr_type = {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str,
                }
        for attribute, data_type in attr_type.items():
            self.assertEqual(type(getattr(self.user, attribute)), data_type)


if __name__ == "__main__":
    unittest.main()
