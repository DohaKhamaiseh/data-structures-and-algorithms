import pytest
from graph import *


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

    expected = ["A","B"]
    lis = []
    for vertex in g.get_vertices() :
     lis.append(vertex.value)
    actual = lis
    assert expected == actual 

def test_get_neighbors():
    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")

    g.add_edge(a,b)

    expected = "B"
    actual = g.get_neighbors(a)[0].vertex.value

    assert expected == actual 

# ## test 5 optional because I didn't put weight

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

def test_business_trip_none1():

    g = Graph()

    a = g.add_vertex("Pandora")
    b = g.add_vertex("Arendelle")
    c = g.add_vertex("Metroville")
    d = g.add_vertex("Monstropolis")
    e = g.add_vertex("Narnia")
    f = g.add_vertex("Naboo")
    
    expected = None
    actual = business_trip(g,["Naboo", "Pandora"])
    
    assert expected == actual

def test_business_trip_none2():

    g = Graph()

    a = g.add_vertex("Pandora")
    b = g.add_vertex("Arendelle")
    c = g.add_vertex("Metroville")
    d = g.add_vertex("Monstropolis")
    e = g.add_vertex("Narnia")
    f = g.add_vertex("Naboo")
    
    expected = None
    actual = business_trip(g,["Narnia", "Arendelle", "Naboo"])
    
    assert expected == actual

def test_business_trip():

    g = Graph()

    a = g.add_vertex("Pandora")
    b = g.add_vertex("Arendelle")
    c = g.add_vertex("Metroville")
    d = g.add_vertex("Monstropolis")
    e = g.add_vertex("Narnia")
    f = g.add_vertex("Naboo")

    g.add_edge(a,b,150)
    g.add_edge(a,c,82)
    g.add_edge(b,c,99)
    g.add_edge(b,d,42)
    g.add_edge(c,d,105)
    g.add_edge(c,e,37)
    g.add_edge(d,f,73)
    g.add_edge(c,f,26)
    g.add_edge(e,f,250)
    
    expected = "$115"
    actual = business_trip(g,["Arendelle","Monstropolis", "Naboo"])
    
    assert expected == actual
