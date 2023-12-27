import pytest
import os
from phonebook import Phonebook

"""
execute: python -m pytest <filename>.py
"""

@pytest.fixture(autouse=True)
def phonebook():
    phonebook = Phonebook(os.getcwd())
    yield phonebook
    phonebook.close()

def test_lookup_by_name(phonebook):
    assert "12345" == phonebook.lookup("Winter")

def test_phonebook_contains_all_names(phonebook):
    assert "Winter" in phonebook.names()

def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Winters")
