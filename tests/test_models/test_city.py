#!/usr/bin/python3
""" unittest for City"""
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel
from models.city import City
import os
import unittest


class TestCity(unittest.TestCase):
    """tests the City class """

    @classmethod
    def setUp(cls):
        """ setting up class for city"""
        cls.city = City()
        cls.city.name = "Nevada"
        cls.city.state_id = "NE"

    @classmethod
    def teardown(cls):
        """deletes setup"""
        del cls.city

    def tearDown(self):
        """ tests the tear down method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_city_doc(self):
        """tests docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_city_attribute(self):
        """tests attributes"""
        attributes = ['state_id', 'id', 'created_at', 'updated_at', 'name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.city, attribute))

    def test_city_subclass(self):
        """tests the subclass method"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_city_save(self):
        """tests the save method"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_city_to_dict(self):
        """tests to_dict method"""
        self.assertEqual('to_dict' in dir(self.city), True)

    def test_city_type(self):
        """tests the attribute type"""
        attr_type = {"state_id": str, "name": str}
        for attribute, data_type in attr_type.items():
            self.assertEqual(type(getattr(self.city, attribute)), data_type)


if __name__ == "__main__":
    unittest.main()
