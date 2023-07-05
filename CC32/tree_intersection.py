class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, root):
        if root is None:
            return []
        else:
            return [root.value] + self.pre_order(root.left) + self.pre_order(root.right)

def tree_intersection(tree1, tree2):
    """
   A function to return the intersection between two Binary Tree
    """
    d = set()
    test = BinaryTree()
    tree1 = test.pre_order(tree1)
    tree2 = test.pre_order(tree2)
    
    if len(tree1) == 0 or len(tree2) == 0:
        return "No intersection"
    
    for node in tree1:
            if node in tree2:
                d.add(node)

    if len(d) ==0 : 
     return "No intersection"

    return d


####################################################3

tree1 = BinaryTree()

Node1 = Node(150)
tree1.root = Node1

Node2 = Node(100)
tree1.root.left = Node2

Node3 = Node(250)
tree1.root.right = Node3

Node4 = Node(75)
tree1.root.left.left = Node4

Node5 = Node(160)
tree1.root.left.right = Node5

Node5_1 = Node(125)
tree1.root.left.right.left = Node5_1

Node5_2 = Node(175)
tree1.root.left.right.right = Node5_2

Node6 = Node(350)
tree1.root.right.right = Node6

Node6_1 = Node(300)
tree1.root.right.right.left = Node6_1

Node6_2 = Node(500)
tree1.root.right.right.right = Node6_2

Node7 = Node(200)
tree1.root.right.left = Node7

################################################3

tree2 = BinaryTree()

Node1_t2 = Node(42)
tree2.root = Node1_t2

Node2_t2 = Node(100)
tree2.root.left = Node2_t2

Node3_t2 = Node(600)
tree2.root.right = Node3_t2

Nodenot_t2 = Node(200)
tree2.root.right.left = Nodenot_t2

Node4_t2 = Node(15)
tree2.root.left.left = Node4_t2

Node5_t2 = Node(160)
tree2.root.left.right = Node5_t2

Node5_1_t2 = Node(125)
tree2.root.left.right.left = Node5_1_t2

Node5_2_t2 = Node(175)
tree2.root.left.right.right = Node5_2_t2

Node6_t2 = Node(350)
tree2.root.right.right = Node6_t2

Node6_1_t2 = Node(4)
tree2.root.right.right.left = Node6_1_t2

Node6_2_t2 = Node(500)
tree2.root.right.right.right = Node6_2_t2

Node7_t2 = Node(200)
tree2.root.right.left = Node7_t2

##########################################################3333
tree_ts= BinaryTree()
tree_ts2= BinaryTree()
result = tree_intersection(tree_ts.root, tree_ts2.root)
print(result)
