# Linked List Implementation


## Approach & Efficiency
*The Node class is used to create individual nodes of the linked list, where each node contains a value and a reference to the next node.*

*The Linked_List class is used to create and manipulate the linked list. It has four methods:*

1. __init__(self): This method initializes the head pointer of the linked list, which initially points to None.

2. insert(self, value): This method inserts a new node at the beginning of the linked list. It creates a new node with the given value and sets its next reference to the current head node. Then, it updates the head pointer to the new node.

3. includes(self, value): This method checks whether a given value is present in the linked list or not. It starts from the head node and traverses the linked list until it finds the value or reaches the end of the list.

4. to_string(self): This method converts the linked list into a string representation. It starts from the head node and traverses the list, appending the value of each node to the output string along with the "->" symbol. It returns the final string.*

## Solution 

1.	value =1    list = {1} -> NULL
2.	value =2    list = {2} -> {1} -> NULL
3.	value =3   list = {3} -> {2} -> {1} -> NULL
4. includes(1)    True
5. includes(5)    False

[Pull Request Link]()
