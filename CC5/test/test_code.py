import pytest
from Code import (Node,Linked_List)

def test_empty_linked_list():
    link = Linked_List()
    actual = link.to_string()
    expected = "Empty Linked List"
    assert expected == actual

def test_insert():
    link = Linked_List()
    link.insert(1)
    actual = link.to_string()
    expected = "{ 1 } -> NULL"
    assert expected == actual

def test_head():
     link = Linked_List()
     link.insert(1)
     actual = link.head.value
     expected = 1
     assert expected == actual

def test_multiple_insert():
     link = Linked_List()
     link.insert(1)
     link.insert(2)
     link.insert(3)
     link.insert(4)
     actual = link.to_string()
     expected = "{ 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
     assert expected == actual

def test_true_including():
     link = Linked_List()
     link.insert(1)
     link.insert(2)
     link.insert(3)
     link.insert(4)
     actual = link.includes(1)
     expected = True
     assert expected == actual

def test_false_including():
     link = Linked_List()
     link.insert(1)
     link.insert(2)
     link.insert(3)
     link.insert(4)
     actual = link.includes(5)
     expected = False
     assert expected == actual

def test_collection():
     link = Linked_List()
     link.insert(2)
     link.insert(4)
     link.insert(6)
     link.insert(8)
     actual = link.to_string()
     expected = "{ 8 } -> { 6 } -> { 4 } -> { 2 } -> NULL"
     assert expected == actual