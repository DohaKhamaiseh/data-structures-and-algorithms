class BinaryTree:
    def __init__(self):
      self.root = None
      self.max = 0
    
    def pre_order(self,root):
   

       if(root is None):
           return []
       else:
          return ([root.value] + self.pre_order(root.left) + self.pre_order(root.right))
    
    def in_order(self,root):


       if(root is None):
           return []
       else:
          return ( self.pre_order(root.left) + [root.value] + self.pre_order(root.right))
    
    def post_order(self,root):

       if(root is None):
           return []
       else:
          return ( self.pre_order(root.left) + self.pre_order(root.right) + [root.value] )
       
    def getMax(self):
       if(self.root is None) : print("The tree you try to find the maximum value of it is empty ^_^")

       else:
         return self.getMax_rec(self.root)
  
    
    def getMax_rec(self,root):
       
       if(root is None): self.max = None
       else:

        if(root.right):
          self.getMax_rec(root.right)
          
        elif(root.left):
            self.getMax_rec(root.left)

        if(root.value>self.max):
           self.max = root.value

        return self.max
    