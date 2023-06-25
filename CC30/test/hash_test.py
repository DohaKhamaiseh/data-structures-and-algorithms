import pytest
from hash import hashtable

def test_set():
    h = hashtable(1)
    actual = h.set("Doha","Sun")
    expected = None

    assert expected == actual 

def test_get():
    h = hashtable(1)
    h.set("Doha","Sun")
    actual = h.get("Doha")
    expected = "Sun"

    assert expected == actual 

def test_key():
    h = hashtable(1)
    h.set("Doha","Sun")
    actual = h.get("hello")
    expected = None

    assert expected == actual 


def test_all_keys():
    h = hashtable(4)
    h.set("Doha","Sun")
    h.set("Saba","Wind")
    h.set("Saja","Calmness")
    h.set("Eman","Faith")

    actual = h.keys()
    expected = ['Doha', 'Saba', 'Saja', 'Eman']

    assert expected == actual 

def test_collision():
    # there are 2 pair that have same index=0 Saba, Saja
    
     h = hashtable(2)
     h.set("Saba","Wind")
     h.set("Saja","Calmness")
     h.set("Eman","Faith")

     
     actual = h.keys()
     expected = ['Saba', 'Saja', 'Eman']

     assert expected == actual

def test_get_collision():
     h = hashtable(2)
     h.set("Saba","Wind")
     h.set("Saja","Calmness")
     h.set("Eman","Faith")

     actual = h.get("Saja")
     expected = "Calmness"

     assert expected == actual

def test_hash():
    h = hashtable(2)
    h.set("Doha","Sun")
    actual = h.hash("Doha")
    expected = 0

    assert expected == actual 

  





    

  

