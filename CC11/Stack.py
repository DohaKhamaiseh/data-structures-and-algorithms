from Node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self,value):
        """
        this method  will add a values each time to the top of the stack

        """
        node = Node(value)

        # to check if the Stack is Empty
        if(self.top):
         node.next=self.top

        # the Stack not empty
        self.top=node
        self.size+=1
    
    def pop(self):
        """
        this method  will remove a values each time from the top of the stack

        """
        # to check if the Stack is Empty
        if(self.top is None):
            raise Exception("The Stack is Empty")
        
        # the Stack not empty
        temp = self.top
        self.top=self.top.next
        temp.next = None
        self.size-=1
        return temp.value
    
    def peek(self):
      """
      this method will return the top value in the stack

      """
      # to check if the Stack is empty
      if(self.top is None):
        raise Exception("The Stack is Empty")
      
      return self.top.value
    
    def isEmpty(self):
       """
       this method will check if the stack is empty or not (return a boolean value)

       """
       if(self.top is None):
          return True
       
       return False
    
    def show_nodes(self):
       """
       this method just to see the stack after pushing or popping values
       """
       output=""
       temp=self.top
       while(temp is not None):
          output+=str(temp.value)+"|"
          temp=temp.next
       return output
  
    
    def get_size(self):
       """
       this method will return the size of the stack
       """
       return self.size