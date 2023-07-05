import pytest
from tree_intersection import *


def test_empty():
   
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    expected = "No intersection"
    actual = tree_intersection(tree1.root,tree2.root)

    assert expected == actual 

def test1():
    
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    tree2.root=Node(1)
    tree2.root.right = Node(2)
    tree2.root.left = Node(3)

    expected = "No intersection"
    actual = tree_intersection(tree1.root,tree2.root)

    assert expected == actual 

def test2():
   
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    tree1.root=Node(1)
    tree1.root.right = Node(2)
    tree1.root.left = Node(3)

    tree2.root=Node(4)
    tree2.root.right = Node(5)
    tree2.root.left = Node(6)

    expected = "No intersection"
    actual = tree_intersection(tree1.root,tree2.root)

    assert expected == actual 

def test3():

    tree1.root=Node(1)
    tree1.root.right = Node(2)
    tree1.root.left = Node(3)

    tree2.root=Node(3)
    tree2.root.right = Node(5)
    tree2.root.left = Node(1)
   
    expected = {1,3}
    actual = tree_intersection(tree1.root,tree2.root)
    assert expected == actual 

