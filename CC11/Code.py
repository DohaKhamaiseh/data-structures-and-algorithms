# from Node import Node
from Stack import Stack

class pseudo_queue :
    def __init__(self, Stackk):
          self.Stackk = Stackk
          self.stack2 = Stack()

    def enqueue(self,value):
        """
        this method will insert a value into the PseudoQueue, using a first-in, first-out approach which is stack's approach
        """
        while(self.Stackk.top is not None):
            self.stack2.push(self.Stackk.pop())
            
        self.stack2.push(value)

    def dequeue(self):
        """
        this method will extract(delete) a value from the PseudoQueue, using a first-in, first-out approach which is stack's approach
        """
        output = ""
        
        last=0
        
        # temp = self.stack2.top

        if(self.stack2.top is None):
            return "no thing to delete"
        if(self.stack2.top.next is None):
            output = "[]"
        
        while(self.stack2.top.next is not None ):
            output +="["+str(self.stack2.top.value)+"]->"
            self.stack2.top = self.stack2.top.next
            # continue
           
        print(output)
        last = self.stack2.pop()
        return last

    
       
    
    def show_nodes(self):
       """
       this method just to see the stack after pushing or popping values
       """
       output=""
       temp=self.stack2.top
    #    print(temp)
       if(temp is None):
            return "Empty Queue"
       
       while(temp is not None):
          if(temp.next is None):
               output+="["+str(temp.value)+"]"
               break
          
          output+="["+str(temp.value)+"]->"
          temp=temp.next
    #    print(output)
       
       return output


  
        
