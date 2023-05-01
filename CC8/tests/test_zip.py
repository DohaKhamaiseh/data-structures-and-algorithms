import pytest
from Code import Linked_List

def test_lists_with_same_length():
    list1 = Linked_List()
    list2 = Linked_List()
    list_zip = Linked_List()

    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2.append(5)
    list2.append(9)
    list2.append(4)

    list_zip.zipLists(list1,list2)

    actual = str(list_zip)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> null"
    assert expected == actual

def test_lists_with_different_length():
    list1 = Linked_List()
    list2 = Linked_List()
    list_zip = Linked_List()

    list1.append(1)
    list1.append(3)
    

    list2.append(5)
    list2.append(9)
    list2.append(4)

    list_zip.zipLists(list1,list2)

    actual = str(list_zip)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> null"
    assert expected == actual

def test_one_empty_list():
    list1 = Linked_List()
    list2 = Linked_List()
    list_zip = Linked_List()

    list1.append(1)
    list1.append(3)
    list1.append(2)

    list_zip.zipLists(list1,list2)

    actual = str(list_zip)
    expected = "{ 1 } -> { 3 } -> { 2 } -> null"
    assert expected == actual

def test_two_empty_lists():
    list1 = Linked_List()
    list2 = Linked_List()
    list_zip = Linked_List()

    list_zip.zipLists(list1,list2)

    actual = str(list_zip)
    expected = "Empty Linked List"
    assert expected == actual



# @pytest.fixture
# def link():
#     link = Linked_List()
#     link.append(1)
#     link.append(3)
#     link.append(8)
#     link.append(2)
#     return link