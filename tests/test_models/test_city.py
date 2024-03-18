#!/usr/bin/python3
"""unittest for City """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8


class test_City(test_basemodel):
    """unittest for City"""

    def __init__(self, *args, **kwargs):
        """unittest initializaton """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """unittest state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """unittest name """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """unittest for style"""
        style = pep8.StyleGuide(quiet=True)
        pycode = style.check_files(["models/city.py"])
        self.assertEqual(pycode.total_errors, 0, "fix pep8")

    def test_db_doc(self):
        """testing docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_db_attribute(self):
        """testing database storage attribute"""
        new_city = City()

        assert type(new_city.id) == str
        assert type(new_city.created_at) == datetime
        assert type(new_city.updated_at) == datetime
        assert hasattr(new_city, "__tablename__")
        assert hasattr(new_city, "name")
        assert hasattr(new_city, "state_id")

        if type(models.storage) != FileStorage:
            self.skipTest("Testing FileStorage")

    def test_dbcity_subclass(self):
        """tests if city is a subclass of basemodel"""
        assert issubclass(City, BaseModel)


if __name__ == "__main__":
    unittest.main()
