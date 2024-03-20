#!/usr/bin/python3
"""unittest Amenity"""
from tests.test_models.test_base_model import TestBaseModel
from models.base_model import BaseModel
from models.amenity import Amenity
import os
import unittest


class TestAmenity(unittest.TestCase):
    """ tests the class Amenity"""

    @classmethod
    def setUp(cls):
        """ setting up class for amentiy"""
        cls.amenity = Amenity()
        cls.amenity.name = "WiFi"

    @classmethod
    def teardown(cls):
        """deletes setup"""
        del cls.amenity

    def tearDown(self):
        """ tests the tear down method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_amenity_doc(self):
        """tests docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_amenity_attribute(self):
        """tests attributes"""
        attributes = ['id', 'created_at', 'updated_at', 'name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.amenity, attribute))

    def test_amenity_subclass(self):
        """tests the subclass method"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_amenity_save(self):
        """tests the save method"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_amenity_to_dict(self):
        """tests to_dict method"""
        self.assertEqual('to_dict' in dir(self.amenity), True)

    def test_amenity_type(self):
        """tests the attribute type"""
        attr_type = {"name": str}
        for attribute, data_type in attr_type.items():
            self.assertEqual(type(getattr(self.amenity, attribute)), data_type)


if __name__ == "__main__":
    unittest.main()
