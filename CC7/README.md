# Linked List Kth

## Whiteboard Process
![](./CC7.PNG)

## Approach & Efficiency
*The Node class is used to create individual nodes of the linked list, where each node contains a value and a reference to the next node.*

*The Linked_List class is used to create and manipulate the linked list. It has one new method:*

**kth_from_end(self, k)**: This method will return the node's value that is k places from the tail of the linked list. in details:
The first part of the code is checking if the entered index k is a valid index in the linked list. If k is greater than the length of the linked list, an exception is raised. If k is equal to the length of the linked list, another exception is raised since there is no node with that index. If k is negative, an exception is also raised since it's an invalid index.


If k is a valid index, the code proceeds to find the node at the index k from the end of the linked list. The method starts by initializing a current variable to the head of the linked list, a node index variable to length - k - 1, and a current index variable to 0. It then iterates through the linked list using a while loop until it reaches the end of the list. In each iteration, it checks if node_idx is equal to current_idx. If they are equal, the method returns the current.value. Otherwise, it moves on to the next node by setting current to current.next and increments current_idx by 1.

if there is just one element in the linked list  the current.next will be None  in that time return the first and only element

## Solution 

list = {1} -> {3} -> {8} -> {2} -> X
1.  K=0      value = 2
2.  K=2       value = 3
3.  K=1       Happy Path
4.  K=6       Sorry, K is bigger than the length of the linked list
5.  K=-1      Sorry, K is referred to as an index and it must be positive


[Pull Request Link](https://github.com/DohaKhamaiseh/data-structures-and-algorithms/pull/11)

