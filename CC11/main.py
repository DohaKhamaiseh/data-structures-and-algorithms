from Stack import Stack
from Code import pseudo_queue


if __name__ == "__main__":
  
    Stackk = Stack()
    Stackk.push(10)
    Stackk.push(15)
    Stackk.push(20)

    pseudo_queuee = pseudo_queue(Stackk)
    pseudo_queuee.enqueue(5)

    print(pseudo_queuee.show_nodes())
    # print(pseudo_queuee.stack2.peek())
    print(pseudo_queuee.dequeue())


    # print(pseudo_queuee.show_nodes())