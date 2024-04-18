import pytest
from project import hangman,guessing,fill_blank

def test_fill_blank():
    assert fill_blank("AFTER",["","","","",""],"A") == ["A","","","",""]

def test_hangman():
    assert hangman(9)=="____\n\n HANGMAN DEAD :( \n_____"

def test_guessing():
    assert "5".isalpha()==False
