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
         global  length
         node = Node(value)

         if self.head is None:
            self.head = node
            length =1

         else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            length+=1

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
            
           output += "null"  
         return output
     
     def zipLists(self,list1, list2):
         pointer1 = list1.head
         pointer2 = list2.head
         
         while pointer1 is not None and pointer2 is not None:
             self.append(pointer1.value)
             self.append(pointer2.value)
             pointer1=pointer1.next
             pointer2=pointer2.next

         

         while pointer1 is not None:
             self.append(pointer1.value)
             pointer1=pointer1.next
            
         while pointer2 is not None:
             self.append(pointer2.value)
             pointer2=pointer2.next
         
         return self

  

if __name__ == "__main__" :

    # test instantiate an empty linked list 
    list1 = Linked_List()
    list2 = Linked_List()
    list_zip = Linked_List()
    
    # list1 : {1} -> {3} -> {2} -> null
    list1.append(1)
    list1.append(3)
    list1.append(2)

    print(list1)

    
    # list2 : {5} -> {9} -> {4} -> null
    list2.append(5)
    list2.append(9)
    list2.append(4)

    print(list2)

    # zip_lists : {1} -> {5} -> {3} -> {9} -> {2} -> {4} -> null
    print(list_zip.zipLists(list1, list2))
