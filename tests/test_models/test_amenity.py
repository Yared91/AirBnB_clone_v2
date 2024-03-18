#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """unittest for style"""
        style = pep8.StyleGuide(quiet=True)
        pycode = style.check_files(["models/city.py"])
        self.assertEqual(pycode.total_errors, 0, "fix pep8")

    def test_dbamenity_attribute(self):
        """testing amenity database storage attribute"""
        new_amenity = Amenity(email="xx", password="xx")

        assert type(new_amenity.id) == str
        assert type(new_amenity.created_at) == datetime
        assert type(new_amenity.updated_at) == datetime
        assert hasattr(new_amentiy, "__tablename__")
        assert hasattr(new_amentiy, "name")
        assert hasattr(new_amentiy, "place_amenities")

        if type(models.storage) != FileStorage:
            self.skipTest("Testing FileStorage")

    def test_dbamentiy_doc(self):
        """tests docstrings in amenity"""
        self.assertIsNotNone(Amenity.__doc__)
    
    def test_dbamenity_subclass(self):
        """tests if amenity is the subclass of basemodel"""
        assert issubclass(Amenity, BaseModel)

if __name__ == "__main__":
    unittest.main()
