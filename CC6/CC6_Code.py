
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

     """ this method will insert a new value before selected value"""
     def insert_before(self,value,new_value):
           node = Node(new_value)
           current = self.head

           if self.head is None:
            self.head = node

              
           else:
             # this condition  will check if the selected value is the first value so to insert before it
             if self.head.value==value:
               self.head = node
               node.next = current

             current = self.head
             temp = None

             while current.next is not None and current.next.value!=value:
                current = current.next

             # this condition will check if the selected value to insert before it is not in the list 
             if (current.next==None):
                raise ValueError("The value " + str(value) + " is not in the list")
             
             # this condition will insert the new value while the selected value not the first value 
             else:
                  temp = current.next
                  current.next = node
                  node.next = temp
                
     """ this method will insert a new value after selected value"""
     def insert_after(self,value,new_value):
          node = Node(new_value)

          if self.head is None:
            self.head = node

          current = self.head
          while current.next is not None and current.value!=value:
                current = current.next

          # this condition will check if the new value to insert is after the last value
          if (current.next==None and current.value==value):   
               current.next = node
               node.next = None    
          # this condition will check if the selected value not in the list so raise an exception
          elif (current.next==None and current.value!=value) :
                raise ValueError("The value " + str(value) + " is not in the list")

          # this condition will insert the new value while the selected value not the last value  
          else:
                  temp = current.next 
                  current.next = node
                  node.next = temp
                  

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
              # "{ a } -> { b } -> { c } -> NULL"
              output += "{ "+ str(current.value) + " } -> "
              current=current.next
            
           output += "X"  
         return output
      

if __name__ == "__main__" :

    # test instantiate an empty linked list 
    test_link_list = Linked_List()
    print( test_link_list)
   

    # test append method
    # test_link_list.append(1)
    # test_link_list.append(2)
    # test_link_list.append(3)
    # test_link_list.append(4)

    # print( test_link_list)

    # # test import
    # # test_link_list.insert_before(3,0)
    # test_link_list.insert_after(5,0)
    # print( test_link_list.to_string())