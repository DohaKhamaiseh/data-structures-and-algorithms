import pytest
from left_join import left_join


def test_empty():
   
    h1 = {}
    h2 = {}

    expected = "No join"
    actual = left_join(h1,h2)

    assert expected == actual 

def test1():
    
    h1 = {}
    h2 = {"diligent":"employed"}

    expected = "No join"
    actual = left_join(h1,h2)

    assert expected == actual 

def test2():
   
    h1 = {"guide":"follow"}
    h2 = {"diligent":"employed"}

    expected = [["guide","follow",None]]
    actual = left_join(h1,h2)

    assert expected == actual 

def test3():

    h1 = {"diligent":"employed", "fond":"enamored", "guide":"usher", "outfit":"garb", "wrath":"anger"}

    h2 = {"diligent":"idle", "fond":"averse", "guide":"follow", "flow":"jam", "wrath":"delight"}


    expected = [['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outfit', 'garb', None], ['wrath', 'anger', 'delight']]
    actual = left_join(h1,h2)

    assert expected == actual 
