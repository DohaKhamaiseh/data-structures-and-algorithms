import pytest
from graph import Graph


def test_added_vertex():
   
    g = Graph()

    expected = "A"
    actual = g.add_vertex("A").value

    assert expected == actual 

def test_added_edge():
    
    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")



    expected = None
    actual = g.add_edge(a,b)

    assert expected == actual 

def test_get_vertices():
   
    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")

    expected = " A ---> B --->"
    actual = g.get_vertices()

    assert expected == actual 

def test_get_neighbors():
    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")

    g.add_edge(a,b)

    expected = " B --->"
    actual = g.get_neighbors(a)

    assert expected == actual 

## test 5 optional because I didn't put weight

def test_size():
    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")

    expected = 2
    actual = g.get_size() 

    assert expected == actual 

