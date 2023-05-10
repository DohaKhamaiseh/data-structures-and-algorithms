from Node import Node
class Queue:
    def __init__(self):
        self.front = None
        # rear = None
        self.back = None
        self.size=0
    
    def enqueue(self,value):
      """
      this method will add a values each time to the end(back) of the queue

      """
      node = Node(value)
      # to check if the Queue is empty
      if(self.front is None):
         self.front = node
         self.back = node

      # not empty
      else:
         self.back.next = node
         self.back=node
      self.size+=1

    def dequeue(self):
      """
      this method will remove a values each time from the start(front) of the queue
      """
      # to check if the Queue is empty
      if(self.front is None):
        raise Exception("The Queue is Empty")
      
      # to check if the Queue contains one node
      if(self.front==self.back):
        self.back = None
        
      # the Queue contains more than one node
      temp = self.front
      self.front = self.front.next 
      temp.next = None
      
      self.size-=1
      return temp.value
    
    def peek(self):
      """
      this method will return the front value in the queue
      """
      # to check if the Queue is empty
      if(self.front is None):
        raise Exception("The Queue is Empty")
      
      return self.front.value
    
    def isEmpty(self):
       """
       this method will check if the queue is empty or not (return a boolean value)
       """
       if(self.front is None):
          return True
       
       return False
    
    def show_nodes(self):
       """
       this method just to see the queue after enqueuing or dequeuing values
       """
       output=""
       temp=self.front
       while(temp is not None):
          output+=str(temp.value)+"|"
          temp=temp.next
       return output
    
    def get_size(self):
       """
       this method will return the size of the queue
       """
       return self.size