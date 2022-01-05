import random

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         else:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
      else:
         self.data = data
# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
howMany = int(input('Set how many numbers: '))
beg = int(input('Set beginning number: '))
end = int(input('Set end number: '))
root = Node(random.randint(beg, end))
for i in range(howMany):
    root.insert(random.randint(beg, end))
numbers = root.inorderTraversal(root)