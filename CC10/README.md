# Linked List Kth

## Whiteboard Process
### Stack
![Push](./CC7.PNG)
![Pop](./CC7.PNG)

### Queue
![Enqueue](./CC7.PNG)
![Dequeue](./CC7.PNG)

## Approach & Efficiency
*The Node class is used to create individual nodes of a Stack or Queue, where each node contains a value and a reference to the next node.*

*The **Stack** class is used to create and manipulate a stack. It has multiple methods:*

 **push(self,value):** it will add a values each time to the top of the stack

 **pop(self):** it will remove a values each time from the top of the stack

 **peek(self);** it will return the top value in the stack

 **isEmpty(self):** it will check if the stack is empty or not (return a boolean value)


 *The **Queue** class is used to create and manipulate a queue. It has multiple methods:*

 **enqueue(self,value):** it will add a values each time to the end(back) of the queue

 **dequeue(self):** it will remove a values each time from the start(front) of the queue

 **peek(self);** it will return the front value in the queue

 **isEmpty(self):** it will check if the queue is empty or not (return a boolean value)



## Solution 
### stack
push(2)
push(4)
push(8)
stack = 8
        4
        2

pop() ----> stack=4
                  2

peek() ----> value = 4

isEmpty() ----> False

### queue
enqueue(2)
enqueue(4)
enqueue(8)
queue = 2|4|8

dequeue() ----> queue=4|8

peek() ----> value = 4

isEmpty() ----> False


[Pull Request Link](https://github.com/DohaKhamaiseh/data-structures-and-algorithms/pull/15)