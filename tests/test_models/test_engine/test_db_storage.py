#!usr/bin/python3
"""Unittest for DB_storage"""

import models
import MySQLdb
import unittest
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


class TestDBStorage(unittest.TestCase):
    """ Unittest for DBStorage"""
    storage = getenv('HBNB_TYPE_STORAGE')

    @classmethod
    def setUpClass(cls):
        """ starting the DBStorage testing"""
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()

            cls.state = State(name="California")
            cls.city = City(name="Addis_Ababa", state_id=cls.state.id)
            cls.user = User(email="Yared@Alx.com", password="Cool")
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                    name="BestSchool")
            cls.amenity = Amenity(name="Wifi")
            cls.review = Review(place_id=cls.place.id,
                    user_id=cls.user.id, text="Elelta")

            lists = [cls.state, cls.city, cls.user, cls.place, cls.amenity, cls.review]
            cls.storage._DBStorage__session.add_all(lists)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """Testing the teardown in DBStorage"""
        if isinstance(models.storage, DBStorage):
            """deleting objects in a loop"""
            for model in (cls.state, cls.city, cls.user,
                    cls.amenity, cls.review):
                cls.storage._DBStorage__session.delete(model)
                cls.storage._DBStorage__session.commit()
            for attr in [cls.state, cls.city, cls.user,
                    cls.place, cls.amenity, cls.review]:
                delattr(cls, attr)
                cls.storage._DBStorage__session.close()
                del cls.storage

    def test_init(self):
        """testing the init method """
        self.assertIsInstance(self.storage, DBStorage)

    def test_doc_db(self):
        """ testing for doc strings """
        methods = ['__init__', 'all', 'new', 'save', 'delete', 'reload']

        for method in methods:
            self.assertIsNotNone(getattr(DBStorage, method).__doc__)

    @unittest.skipIf(type(models.storage) == FileStorage,
            "Testing FileStorage")

    def test_all(self):
        """ testing all methods"""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(len(self.storage.all()), 6)

    @unittest.skipIf(type(models.storage) == FileStorage,
            "Testing FileStorage")

    def test_new(self):
        """testing the new method"""
        new_state = State(name="Asmara")
        self.storage.new(new_state)
        add_state = list(self.storage._DBStorage__session.new)
        self.assertIn(new_state, add_state)

    @unittest.skipIf(type(models.storage) == FileStorage,
            "Testing FileStorage")

    def test_save(self):
        """testing the save method"""
        add_state = State(name="Nairobi")
        """Add the state object to the session and save it"""
        self.storage._DBStorage__session.add(add_state)
        self.storage.save()
        """ connects to test MySQL database using my SQLdb"""
        stores = MySQLdb.connect(user="Best_school",
                passwd="hbnb_test_pwd", db="hbnb_test_db")
        """creating a cursor object to execute SQL queries"""
        create = db.cursor()
        """
        Execute a SQL query to select all columns from
        the 'states' table where the name is 'Nairobi'
        """
        cursor.excute("SELECT * FROM states WHERE BINARY name = 'Nairobi'")
        fetch = cursor.fetchall()
        self.assertEqual(1, len(fetch))
        self.assertEqual(state.id, fetch[0][0])
        curser.close()

    @unittest.skipIf(type(models.storage) == FileStorage,
            "Testing FileStorage")

    def test_delete(self):
        """testing the delete method"""
        delete_st = State(name="Kampala")
        self.storage._DBStorage__session.add(delete_st)
        self.storage._DBStorage__session.commit()

        self.storage.delete(delete_st)
        lists = list(self.storage._DBStorage__session.deleted)
        self.assertIn(delete_st, lists)

    @unittest.skipIf(type(models.storage) == FileStorage,
            "Testing FileStorage")

    def test_dbstorage_methods(self):
        """testing the core DBStorage methods exist"""
        expected_methods = ["__init__", "all", "new", "save",
                "delete", "reload"]
        """checking if all methods is present """
        for method in expected_methods:
            self.assertTrue(hasattr(DBStorage, method),
                    f"Method {method} not found in DBStorage")

    @unittest.skipIf(type(models.storage) == FileStorage,
            "Testing FileStorage")

    def test_dbstorage_attributes(self):
        """Testing that DBStorage has expected attributes."""
        self.assertIsInstance(self.storage._DBStorage__engine, Engine)
        self.assertIsInstance(self.storage._DBStorage__session, Session)

    def test_reload(self):
        """testing reload methods"""
        old_session = self.storage._DBStorage__session
        new_session = self.storage.reload()

        self.assertIsInstance(new_session, Session)
        self.assertNotEqual(old_session, new_session)
        new_session.close()
        self.storage._DBStorage__session = old_session

    @unittest.skipIf(type(models.storage) == FileStorage,
            "Testing FileStorage")


if __name__ == '__main__':
    unittest.main()
