#!/usr/bin/python3
""" unittest for basemodel"""
from models.base_model import BaseModel
from models.base_model import Base
import unittest
from datetime import datetime
from uuid import UUID
import json
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
        'basemodel test not supported')


class test_basemodel(unittest.TestCase):
    """testing basemodel"""

    def __init__(self, *args, **kwargs):
        """initializing basemodel """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ setting up class for basemodel"""
        pass

    def tearDown(self):
        """ tests the tear down method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_init(self):
        """unittest for initialization of basemodel"""
        self.assertIsInstance(self.value(), BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_default(self):
        """ testing default method"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """testing kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ testing kwargs with integer argument"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ testing str for basemodel"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ testing to dict method for basemodel"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ testing kwargs without argument"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ testing kwargs with one argument"""
        n = {'name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.name, n['name'])

    def test_id(self):
        """testing the id method """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ testing created method"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """testing updated method"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_dbbase_doc(self):
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


if __name__ == "__main__":
    unittest.main()
