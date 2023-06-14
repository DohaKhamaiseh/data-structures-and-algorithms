import pytest
from merge import Mergesort

def test_1():

    arr = [20,18,12,8,5,-2]
    actual = Mergesort(arr)
    expected = [-2, 5, 8, 12, 18, 20]
  
    assert actual == expected

def test_2():

    arr = [5,12,7,5,5,7]
    actual = Mergesort(arr)
    expected = [5, 5, 5, 7, 7, 12]
  
    assert actual == expected

def test_3():

    arr = []
    actual = Mergesort(arr)
    expected = []
  
    assert actual == expected

def test_4():

    arr = [8,4,23,42,16,15]
    actual = Mergesort(arr)
    expected = [4, 8, 15, 16, 23, 42]
  
    assert actual == expected


def test_5():

    arr = [2,3,5,7,13,11]
    actual = Mergesort(arr)
    expected = [2, 3, 5, 7, 11, 13]
  
    assert actual == expected
