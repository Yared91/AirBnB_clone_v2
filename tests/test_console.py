#!/user/bin/python3
"""Unittest for Console"""
import unittest
from unittest.mock import patch
import os
import console
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
	"""testing the Console"""
	@classmethod
	def setUpClass(cls):
		"""setign up test console"""
		cls.console = HBNBCommand

	@classmethod
	def teardown(cls):
		"""deleting setup tests"""
		del cls.console

	def tearDown(self):
		"""remove json files """
		if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
			try:
			    os.remove("file.json")
			except Exception:
			    pass

	def test_console_doc(self):
		"""testing doc in console"""
		methods = [console.__doc__, HBNBCommand.emptyline.__doc__,
		    HBNBCommand.do_quit.__doc__, HBNBCommand.do_EOF.__doc__,
		    HBNBCommand.do_create.__doc__,
		    HBNBCommand.do_show.__doc__,
		    HBNBCommand.do_destroy.__doc__,
		    HBNBCommand.do_all.__doc__,
		    HBNBCommand.do_update.__doc__,
		    HBNBCommand.do_count.__doc__,
		]
		self.asserttrue(all(method is not None for method in methods))

	def test_console_quit(self):
	    """ testing the quit method"""
	    with patch('sys.stdout', new=StringIO()) as fb:
	     self.console.onecmd("quit")
	     self.assertEqual('', fb.getvalue())

	def test_console_EOF(self):
	     """testing the EOF method """
	     with patch('sys.stdout', new=StringIO()) as fb:
		  self.assertTrue(self.console.onecmd("EOF"))

if __name__ == "__main__":
   unittest.main()
