#!usr/bin/python3
"""tests db storage"""

import unittest
import os
import MySQLdb
from models.engine.db_storage import DBStorage
from models.state import State


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not FileStorage')
class TestDBStorage(unittest.TestCase):
    """testing DBStorage class"""

    @classmethod
    def SetUpClass(self):
        """setsup db storage test"""
        self.User = getenv("HBNB_MYSQL_USER")
        self.Passwd = getenv("HBNB_MYSQL_PWD")
        self.Db = getenv("HBNB_MYSQL_DB")
        self.Host = getenv("HBNB_MYSQL_HOST")
        self.db = MySQLdb.connect(host=self.Host, user=self.User,
                passwd=self.Passwd, db=self.Db, charset="utf8")
        self.query = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def teardown(self):
        """deletes the created table"""
        self.query.close()
        self.db.close()

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not FileStorage')
    def test_query_table(self):
        """tests the query table"""
        self.query.execute("SHOW TABLE")
        show = self.query.fetchall()
        self.assertEqual(len(show), 7)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not FileStorage')
    def test_empty_table_user(self):
        """checks for columns of table in User"""
        self.query.execute("SELECT * FROM users")
        show = self.query.fetchall()
        self.assertEqual(len(show), 0)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not FileStorage')
    def test_empty_table_cities(self):
        """checks for columns of table in cities"""
        self.query.execute("SELECT * FROM cities")
        show = self.query.fetchall()
        self.assertEqual(len(show), 0)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not FileStorage')
    def test_add(self):
        """adds new entries"""
        self.query.execute("SELECT * FROM states")
        rows = self.query.fetchall()
        self.assertEqual(len(rows), 0)
        """ add a new state to the database"""
        new_state = State(name="NewYork")
        new_state.save()
        self.db.autocommit(True)

        """check if the query now results 1 row after adding a state"""
        self.query.execute("SELECT * FROM states")
        rows = self.query.fetchall()
        self.assertEqual(len(rows), 1)


if __name__ == "__main__":
    unittest.main()
