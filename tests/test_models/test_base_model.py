#!/usr/bin/python3
""" unittest for basemodel"""
from models.base_model import BaseModel
from models.base_model import Base
import unittest
from datetime import datetime
from uuid import UUID
import json
import os
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """testing basemodel"""

    @classmethod
    def setUp(cls):
        """ setting up class for basemodel"""
        cls.base = BaseModel()
        cls.base.name = "Elilta"
        cls.base.number = 60

    @classmethod
    def teardown(cls):
        """deletes setup"""
        del cls.base

    def tearDown(self):
        """ tests the tear down method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_base_doc(self):
        """tests docstrings"""
        doc = [
            BaseModel,
            BaseModel.__init__,
            BaseModel.save,
            BaseModel.to_dict,
            BaseModel.delete,
            BaseModel.__str__,
            ]
        for objects in doc:
            self.assertTrue(hasattr(objects, "__doc__"),
                    f"{objects.__name__} missing docstring")

    def test_base_method(self):
        """tests methods"""
        methods = ["__init__", "save", "to_dict"]

        methods_present = all(hasattr(BaseModel, method) for method in methods)
        self.assertTrue(methods_present)

    def test_base_init(self):
        """tests the init method"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not FileStorage')

    def test_base_save(self):
        """tests the save method"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_base_to_dict(self):
        """tests to_dict method"""
        dictionary = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(dictionary['created_at'], str)
        self.assertIsInstance(dictionary['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
