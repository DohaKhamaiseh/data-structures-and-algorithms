"""This class is to create nodes which are the elements of any linked list"""
class Node :
    def __init__(self, value):
        """this method intializes the value and the next pointer that each node has"""
        self.value = value
        self.next = None

"""This class creating a linked list """
class Linked_List:
     """this method intializes the head pointer which points to the fisrt node in the linked list """
     def __init__(self):
         self.head=None
     
     """this method to insert node to the linked list, the node will be inserted on the head of the linked list"""
     def insert(self,value):
         node = Node(value)
         node.next=self.head
         self.head=node
     
     """this method to check if the value is in the linked list or not"""
     def includes(self,value):  
       current= self.head

        # if the linked list is empty
       if(self.head == None):
           return False
       #if the target value is the first value in the linked list
       if(self.head.value==value):
           return True
       # if the target value is not the first value in the linked list
       else:
           current =current.next
           while current is not None:
               if(current.value==value):
                   return True
               current=current.next

           # if the value not in the linkedlist at all
           return False
       
     """this method will print all values in the linked list after check if it is empty or not"""
     def to_string(self):
         output=""
         # if the linked list is empty
         if (self.head==None):
          output =  "Empty Linked List"
         
         # if the linked list not empty
         else : 
           current = self.head
           while(current is not None):
              # "{ a } -> { b } -> { c } -> NULL"
              output += "{ "+ str(current.value) + " } -> "
              current=current.next
            
           output += "NULL"  
         return output

if __name__ == "__main__" :

    # test instantiate an empty linked list 
    test_link_list = Linked_List()
    # print( test_link_list.to_string())
    print( test_link_list)

    # test insert method
    # test_link_list.insert(1)
    # test_link_list.insert(2)
    # test_link_list.insert(3)
    # test_link_list.insert(4)

    # # test to_string method
    # print( test_link_list.to_string())

    # # test includes method
    # print(test_link_list.includes(5))