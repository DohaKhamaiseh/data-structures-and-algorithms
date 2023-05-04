import pytest
from Stack import Stack
from Queue import Queue


############################################  Stack  ##############################################

def test_push_one_value_stack():
    stackk = Stack()
    stackk.push(2)
    expected = "2|"
    actual = stackk.show_nodes()
    assert expected == actual

def test_push_multiple_values_stack():
    stackk = Stack()
    stackk.push(2)
    stackk.push(4)
    stackk.push(8)
    expected = "8|4|2|"
    actual = stackk.show_nodes()
    assert expected == actual


def test_pop_one_value_stack():
    stackk = Stack()
    stackk.push(2)
    actual = stackk.pop()
    expected = 2
    assert expected == actual


def test_pop_multiple_values_stack():
    stackk = Stack()
    stackk.push(2)
    stackk.push(4)
    stackk.push(8)

    stackk.pop()
    stackk.pop()
    stackk.pop()
    
    expected = ""
    actual = stackk.show_nodes()
    assert expected == actual
    
# def case5

def test_instantiate_empty_stack():
    stackk = Stack()
    expected = ""
    actual = stackk.show_nodes()
    assert expected == actual

def test_pop_empty_stack():
 
    stackk = Stack()
    stackk.push(2)
    stackk.push(4)
    stackk.push(8)

    stackk.pop()
    stackk.pop()
    stackk.pop()

    with pytest.raises(Exception):
      stackk.pop()

############################################  Queue  ##############################################

def test_enqueue_one_value_queue():
    queuee = Queue()
    queuee.enqueue(2)
    expected = "2|"
    actual = queuee.show_nodes()
    assert expected == actual

def test_enqueue_multiple_values_queue():
    queuee = Queue()
    queuee.enqueue(2)
    queuee.enqueue(4)
    queuee.enqueue(8)

    expected = "2|4|8|"
    actual = queuee.show_nodes()
    assert expected == actual


def test_dequeue_one_value_queue():
    queuee = Queue()
    queuee.enqueue(2)

    actual = queuee.dequeue()
    expected = 2
    assert expected == actual
      

def test_peek_value_queue():
    queuee = Queue()
    queuee.enqueue(2)

    actual = queuee.peek()
    expected = 2
    assert expected == actual

def test_dequeue_multiple_values_queue():
    queuee = Queue()
    queuee.enqueue(2)
    queuee.enqueue(4)
    queuee.enqueue(8)

    queuee.dequeue()
    queuee.dequeue()
    queuee.dequeue()
    
    expected = ""
    actual = queuee.show_nodes()
    assert expected == actual

def test_instantiate_empty_queue():
    queuee = Queue()
    expected = ""
    actual = queuee.show_nodes()
    assert expected == actual

def test_pop_empty_queue():
 
    queuee = Queue()
    queuee = Queue()
    queuee.enqueue(2)
    queuee.enqueue(4)
    queuee.enqueue(8)

    queuee.dequeue()
    queuee.dequeue()
    queuee.dequeue()

    with pytest.raises(Exception):
       queuee.dequeue()



