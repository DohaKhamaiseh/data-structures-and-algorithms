class BinaryTree:
    def __init__(self):
      self.root = None
      self.max = 0
      self.r = []
    
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
   
    
    def tree_breadth_first(self,root):
      """
      this method will traverse a tree using tree breadth first way (by levels)
      """
      t = []
      listt = []
      if(root is None):
         return
      
      t.append(root)
      while(len(t)>0):
       listt.append(t[0].value)
       r = t.pop(0)
       if(r.left is not None): t.append(r.left)
       if(r.right is not None): t.append(r.right)

      return listt

      #  if(root is not None):
      #   if(root.left is not None and root.right is not None):
      #    self.r.append(root.value)
      #    self.tree_breadth_first(root.left)
      #   self.tree_breadth_first(root.right)
         

      #  else:
      #    #  self.tree_breadth_first(root.left)
      #    # self.r.append(root.value)
      #    # print(root.left)
      #    # print(root.right.value)
      #    self.r.append(root.value)
      #    self.tree_breadth_first(root.right)
      #    # self.tree_breadth_first(root.right)