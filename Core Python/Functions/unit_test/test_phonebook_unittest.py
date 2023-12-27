import os
import unittest
from phonebook import Phonebook

"""
execute: python -m unittest <filename>.py
"""

class PhonebookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = Phonebook(os.getcwd())

    def tearDown(self) -> None:
        self.phonebook.close()

    def test_lookup_by_name(self):
        self.assertEqual("12345", self.phonebook.lookup("Winter"))

    def test_phonebook_contains_all_names(self):
        self.assertIn("Winter", self.phonebook.names())

    def test_missing_name_raises_error(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("Winters")

    @unittest.skip("WIP")
    def test_test(self):
        pass
