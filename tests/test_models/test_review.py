#!/usr/bin/python3
""" unittest for Review"""
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review
import os
import unittest


class TestUser(unittest.TestCase):
    """tests the Review class """

    @classmethod
    def setUp(cls):
        """ setting up class for review"""
        cls.review = Review()
        cls.review.place_id = "123-abc"
        cls.review.user_id = "456-efg"
        cls.review.text = "unittest is cool"

    @classmethod
    def teardown(cls):
        """deletes setup"""
        del cls.review

    def tearDown(self):
        """ tests the tear down method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_review_doc(self):
        """tests docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_review_attribute(self):
        """tests attributes"""
        attributes = ['place_id', 'id', 'created_at', 'updated_at', 'user_id',
                'text']
        for attribute in attributes:
            self.assertTrue(hasattr(self.review, attribute))

    def test_review_subclass(self):
        """tests the subclass method"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_review_save(self):
        """tests the save method"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_review_to_dict(self):
        """tests to_dict method"""
        self.assertEqual('to_dict' in dir(self.review), True)

    def test_review_type(self):
        """tests the attribute type"""
        attr_type = {
                "text": str,
                "place_id": str,
                "user_id": str,
                }
        for attribute, data_type in attr_type.items():
            self.assertEqual(type(getattr(self.review, attribute)), data_type)


if __name__ == "__main__":
    unittest.main()
