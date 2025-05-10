from collections import deque
# Задание 1
class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    def insert( self, root, key):
        if root is None:
            return BinaryTree(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)
bin_tree = BinaryTree(None)
root = None
keys = [10,20,30,40,50,25,27]
s_key = 10
for key in keys:
    root = bin_tree.insert(root, key)
result = bin_tree.search(root,s_key)
if result is None:
    print("Is not")
else:
    print(f"{s_key}")

# Задание 2
def breadth_first_search(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.key, end= " ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
breadth_first_search(root)
# Задание 3
print("")
def  preorder_traversal(root):
    if root:
        print(root.key, end = " ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
preorder_traversal(root)
print("")
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)
inorder_traversal(root)
print("")
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=" ")
postorder_traversal(root)
# Задание 4
print("")
print("Задание 4")
class AVLTree:
    def insert(self, root, key):
        if root is None:
            return BinaryTree(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.rebalance(root)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.right), self.get_height(z.left))
        y.height = 1 + max(self.get_height(y.right), self.get_height(y.left))
        return y
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    def rebalance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
avl_tree = AVLTree()
root = None
keys = [10,20,30,40,50,25,27]
for key in keys:
    root = avl_tree.insert(root,key)
def pre_order(node):
    if not node:
        return
    print(f"{node.key}", end=" ")
    pre_order(node.left)
    pre_order(node.right)
pre_order(root)