
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
    
     """this method to append node to the linked list, the node will be appended to the end of the linked list"""
     def append (self,value):
         node = Node(value)

         if self.head is None:
            self.head = node

         else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

     """ this method is intended for the user to see the linked list after any changes if he/she want"""
     def __str__(self):
         output=""
         # if the linked list is empty
         if (self.head==None):
          output =  "Empty Linked List"
         
         # if the linked list not empty
         else : 
           current = self.head
           while(current is not None):
              # "{ a } -> { b } -> { c } -> X"
              output += "{ "+ str(current.value) + " } -> "
              current=current.next
            
           output += "X"  
         return output
    
     """this method will return the node's value that is k places from the tail of the linked list."""
     def kth_from_end(self, k):
         current = self.head
         list = []
         
        #  list.append(self.head.value)

         while current.next is not None:
             list.append(current.value)
             current = current.next
         list.append(current.value)

        #  print(list)
         rev_list = list[::-1]
        #  print(rev_list)
        # to check if the entered index is not an available index(bigger than the length of the linked list)
         if k>len(rev_list):
             raise Exception("Sorry, K is bigger than the length of linked list")
         
         if k==len(rev_list):
             raise Exception("Sorry, K is equal to the length of linked list, so it's index out of range")
         
         # to check if the entered index is not an index (the index must be positive number)
         if k<0:
           raise Exception("Sorry, K is referred to an index and it must be positive")
         
         for ele in rev_list:
             index = rev_list.index(ele)
             if k == index :
                 return ele
             # to check if the entered index is in the middle index to the linked list
             if k == len(rev_list)//2:
                 return "Happy Path"


if __name__ == "__main__" :

    # test instantiate an empty linked list 
    test_link_list = Linked_List()
    # # print( test_link_list)

    # # test append method
    # test_link_list.append(1)
    # test_link_list.append(3)
    # test_link_list.append(8)
    # test_link_list.append(2)

    # # print( test_link_list)
    # print(test_link_list.kth_from_end(0))
    # # print(test_link_list.kth_from_end(2))
    
    