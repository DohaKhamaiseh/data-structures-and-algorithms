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

    expected = "B"
    actual = g.get_neighbors(a)[0].value

    assert expected == actual 

## test 5 optional because I didn't put weight

def test_size():
    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")

    expected = 2
    actual = g.get_size() 

    assert expected == actual 

def test_breadth_first_no_children():
    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")

    

    expected = ' A'
    actual = g.breadth_first(a) 

    assert expected == actual

def test_breadth_first():
    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")
    c = g.add_vertex("C")
    d = g.add_vertex("D")

    g.add_edge(a,b)
    g.add_edge(a,c)
    g.add_edge(c,b)
    g.add_edge(d,b)
    g.add_edge(d,c)

    expected = ' A B C D'
    actual = g.breadth_first(a) 

    assert expected == actual

def test_breadth_vertex_not_connected():

    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")
    c = g.add_vertex("C")
    d = g.add_vertex("D")
    
    g.add_edge(a,b)
    g.add_edge(a,c)
    g.add_edge(c,b)

    expected = ' A B C'
    actual = g.breadth_first(a) 

    assert expected == actual
