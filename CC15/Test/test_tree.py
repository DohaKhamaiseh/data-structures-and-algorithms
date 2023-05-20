import pytest
from Node import Node
from BinaryTree import BinaryTree
from BST import BST

def test_instantiate__empty_tree():
    tree = BinaryTree()
    expected = []
    actual = tree.pre_order(None)
    assert expected == actual

def test_tree_with_single_root():
    tree = BinaryTree()
    node = Node(10)
    tree.root = node
    expected = [10]
    actual = tree.pre_order(tree.root)
    assert expected == actual

def test_left_child_and_right_child():
    BSTT = BST()
    BSTT.Add(10)
    BSTT.Add(5)
    BSTT.Add(15)
    expected = [10,5,15]
    actual = BSTT.pre_order(BSTT.root)
    assert expected == actual

def test_pre_order():
    BSTT = BST()
    BSTT.Add(10)
    BSTT.Add(5)
    BSTT.Add(15)
    BSTT.Add(3)
    BSTT.Add(6)
    BSTT.Add(12)
    BSTT.Add(20)

    expected = [10, 5, 3, 6, 15, 12, 20]
    actual = BSTT.pre_order(BSTT.root)
    assert expected == actual


def test_in_order():
    BSTT = BST()
    BSTT.Add(10)
    BSTT.Add(5)
    BSTT.Add(15)
    BSTT.Add(3)
    BSTT.Add(6)
    BSTT.Add(12)
    BSTT.Add(20)

    expected = [5, 3, 6, 10, 15, 12, 20]
    actual = BSTT.in_order(BSTT.root)
    assert expected == actual


def test_post_order():
    BSTT = BST()
    BSTT.Add(10)
    BSTT.Add(5)
    BSTT.Add(15)
    BSTT.Add(3)
    BSTT.Add(6)
    BSTT.Add(12)
    BSTT.Add(20)

    expected = [5, 3, 6, 15, 12, 20, 10]
    actual = BSTT.post_order(BSTT.root)
    assert expected == actual

def test_contain_true():
    BSTT = BST()
    BSTT.Add(10)
    BSTT.Add(5)
    BSTT.Add(15)
    BSTT.Add(3)
    BSTT.Add(6)
    BSTT.Add(12)
    BSTT.Add(20)

    expected = True
    actual = BSTT.contains(20)
    assert expected == actual


def test_contain_false():
    BSTT = BST()
    BSTT.Add(10)
    BSTT.Add(5)
    BSTT.Add(15)
    BSTT.Add(3)
    BSTT.Add(6)
    BSTT.Add(12)
    BSTT.Add(20)

    expected = False
    actual = BSTT.contains(4)
    assert expected == actual