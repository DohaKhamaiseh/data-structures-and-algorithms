import pytest
from CC6_Code import (Node,Linked_List)

def test_append_one():
    link = Linked_List()
    link.append(1)
    actual = str(link)
    expected = "{ 1 } -> X"
    assert expected == actual

def test_append_multiple(link):
    actual = str(link)
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> X"
    assert expected == actual

def test_insert_before_middle(link):
    link.insert_before(3,0)
    actual = str(link)
    expected = "{ 1 } -> { 2 } -> { 0 } -> { 3 } -> { 4 } -> { 5 } -> X"
    assert expected == actual

def test_insert_before_first(link):
    link.insert_before(1,0)
    actual = str(link)
    expected = "{ 0 } -> { 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> X"
    assert expected == actual

def test_insert_after_middle(link):
    link.insert_after(3,0)
    actual = str(link)
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 0 } -> { 4 } -> { 5 } -> X"
    assert expected == actual

def test_insert_after_end(link):
    link.insert_after(5,0)
    actual = str(link)
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 0 } -> X"
    assert expected == actual


@pytest.fixture
def link():
    link = Linked_List()
    link.append(1)
    link.append(2)
    link.append(3)
    link.append(4)
    link.append(5)
    return link