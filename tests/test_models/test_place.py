#!/usr/bin/python3
""" unittest for Place"""
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place
import os
import unittest


class TestPlace(unittest.TestCase):
    """tests the place class """

    @classmethod
    def setUp(cls):
        """ setting up class for place"""
        cls.place = Place()
        cls.place.city_id = "678-lkj"
        cls.place.user_id = "987-mnb"
        cls.place.name = "Yared"
        cls.place.description = "God Bless Us"
        cls.place.number_rooms = 100
        cls.place.number_bathrooms = 50
        cls.place.max_guest = 100000
        cls.place.price_by_night = 800
        cls.place.latitude = 120.0
        cls.place.longitude = 150.0
        cls.place.amenity_ids = ["897-bghy"]

    @classmethod
    def teardown(cls):
        """deletes setup"""
        del cls.place

    def tearDown(self):
        """ tests the tear down method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_place_doc(self):
        """tests docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_place_attribute(self):
        """tests attributes"""
        attributes = ['city_id', 'id', 'created_at', 'updated_at', 'user_id',
                'name', 'description', 'number_rooms', 'number_bathrooms',
                'max_guest', 'price_by_night', 'latitude', 'longitude',
                'amenity_ids']
        for attribute in attributes:
            self.assertTrue(hasattr(self.place, attribute))

    def test_place_subclass(self):
        """tests the subclass method"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_place_save(self):
        """tests the save method"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_placer_to_dict(self):
        """tests to_dict method"""
        self.assertEqual('to_dict' in dir(self.place), True)

    def test_place_type(self):
        """tests the attribute type"""
        attr_type = {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list,
                }
        for attribute, data_type in attr_type.items():
            self.assertEqual(type(getattr(self.place, attribute)), data_type)


if __name__ == "__main__":
    unittest.main()
