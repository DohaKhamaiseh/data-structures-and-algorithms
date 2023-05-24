from BinaryTree import BinaryTree
from Node import Node

class BST(BinaryTree) :
    def __init__(self):
         super().__init__()
    
    def Add(self,value):
        
         if (self.root is None):
              self.root = Node(value)
         else: 
            self.add_rec(value,self.root)  
     
    
    def add_rec(self,value,root):
         
         if(value==root.value):
              print("No need to add it")

         elif(value<root.value):
              if(root.left):
                   self.add_rec(value,root.left)
              else:
               root.left = Node(value)  

         elif(value>root.value):
           if(root.right):
                   self.add_rec(value,root.right)
           else:
              root.right = Node(value)  

        
            

    def contains(self,value):
         if(self.root == value) : return True
         else : 
          return self.contains_rec(self.root, value)


    def contains_rec(self,root,value):
          
          if (value == root.value):
              return True
          
          elif(value<root.value):
              if(root.left):
                return self.contains_rec(root.left,value)
              else:
               return False

          else :
           if(root.right):
                return  self.contains_rec(root.right,value)
           else:
              return False


            

    
   



tree_test = BinaryTree()


Node1 = Node(2)
tree_test.root = Node1

Node2 = Node(7)
tree_test.root.left = Node2

Node3 = Node(5)
tree_test.root.right = Node3

Node4 = Node(2)
tree_test.root.left.left = Node4

Node5 = Node(6)
tree_test.root.left.right = Node5

Node5_1 = Node(5)
tree_test.root.left.right.left = Node5_1

Node5_2 = Node(11)
tree_test.root.left.right.right = Node5_2

Node6 = Node(9)
tree_test.root.right.right = Node6

Node6_1 = Node(4)
tree_test.root.right.right.left = Node6_1

# print(tree_test.pre_order(tree_test.root))
# print(tree_test.in_order(tree_test.root))
# print(tree_test.post_order(tree_test.root))


# BST_test = BST()
# BST_test.Add(10)
# BST_test.Add(5)
# BST_test.Add(15)
# BST_test.Add(20)
# BST_test.Add(12)
# BST_test.Add(6)
# BST_test.Add(3)

# print(BST_test.pre_order(BST_test.root))
# print(BST_test.in_order(BST_test.root))
# print(BST_test.post_order(BST_test.root))

# print(BST_test.contains(5))
# print(tree_test.getMax())
print(tree_test.tree_breadth_first(tree_test.root))




