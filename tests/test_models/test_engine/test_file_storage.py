<<<<<<< HEAD
#!/usr/bin/python3
import os
import unittest
from os import path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
""" testing the file storage"""


class TestCaseFileStorage(unittest.TestCase):
    """ class for test cases """

    def setUp(self):
        """ setting up the various
            components for the test """
        self.dir_path = 'file.json'
        self.my_model = FileStorage()

    def tearDown(self):
        """ dispose json file """
        if path.exists(self.dir_path):
            os.remove(self.dir_path)

    def test_all(self):
        """ check type return by all function """
        self.assertEqual(type(self.my_model.all()), dict)

    def test_new(self):
        test_model = BaseModel()
        self.my_model.new(test_model)
        len_dict = len(self.my_model.all())
        self.assertGreater(len_dict, 0)

    def test_save(self):
        """ save content to file
         and create if not exist"""
        self.my_model.save()
        self.assertEqual(path.exists(self.dir_path), True)

    def test_reload(self):
        model = FileStorage()
        self.my_model.reload()
        len_dict = len(model.all())
        self.assertGreater(len_dict, 0)
=======
#!/usr/bin/python3
"""test module for class FileStorage"""

import unittest
import models
import os
import datetime

class Filesorage(unittest.TestCase):
    """class to test the FileStorage class"""

    def test_documentation(self):
        """tests module, class and methods docstring"""
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.__doc__)
        shortcut = models.engine.file_storage.FileStorage
        self.assertIsNotNone(shortcut.__init__.__doc__)
        self.assertIsNotNone(shortcut.all.__doc__)
        self.assertIsNotNone(shortcut.new.__doc__)
        self.assertIsNotNone(shortcut.save.__doc__)
        self.assertIsNotNone(shortcut.reload.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.engine.file_storage.FileStorage()
        self.assertIsInstance(instance, models.engine.file_storage.FileStorage)

    def test_all(self):
        """test all method"""
        instance = models.engine.file_storage.FileStorage()
        dictionary = instance.all()
        self.assertIsNotNone(dictionary)
        self.assertIsInstance(dictionary, dict)
        self.assertIs(dictionary, instance._FileStorage__objects)

    def test_new(self):
        """test new method"""
        dict1 = models.storage.all().copy()
        instance = models.base_model.BaseModel()
        dict2 = models.storage.all().copy()
        self.assertLess(len(dict1), len(dict2))

    def test_save(self):
        """test save method"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))
        instance = models.base_model.BaseModel()
        instance.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """test reload method"""
        instance = models.engine.file_storage.FileStorage()
        dic1 = models.storage.all().copy()
        models.storage.reload()
        dic2 = models.storage.all().copy()
        self.assertEqual(len(dic1), len(dic2))
        instance.save()
        self.assertIsInstance(instance._FileStorage__file_path, str)
        self.assertIsInstance(instance._FileStorage__objects, dict)
        self.assertTrue(os.path.exists("file.json"))


if __name__ == "__main__":
    unittest.main()


>>>>>>> cc1bd00f1ca76611591882c0c790a7e0e53b17b7
