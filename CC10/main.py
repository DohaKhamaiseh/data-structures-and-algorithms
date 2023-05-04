from Stack import Stack
from Queue import Queue

if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(2)
    stack1.push(4)
    stack1.push(8)
    print(stack1.isEmpty())
    # print(stack1.get_size())
    print(stack1.show_nodes())
    
    Queue1 = Queue()
    Queue1.enqueue(16)
    Queue1.enqueue(32)
    Queue1.enqueue(64)
    print(Queue1.isEmpty())
    print(Queue1.show_nodes())