class BinaryTree:
    def __init__(self):
      self.root = None
    
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
       
    