from Node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self,value):
        node = Node(value)

        # to check if the Stack is Empty
        if(self.top):
         node.next=self.top

        # the Stack not empty
        self.top=node
        self.size+=1
    
    def pop(self):
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
      # to check if the Stack is empty
      if(self.top is None):
        raise Exception("The Stack is Empty")
      
      return self.top.value
    
    def isEmpty(self):
       if(self.top is None):
          return True
       
       return False
    
    def show_nodes(self):
       output=""
       temp=self.top
       while(temp is not None):
          output+=str(temp.value)+"|"
          temp=temp.next
       return output
  
    
    def get_size(self):
       return self.size
        