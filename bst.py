# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# Ryan Earl

class BinarySearchTree:
   def __init__(self, key = None): 
      self.left = None
      self.right = None
      self.key = key
      self.parent = None

   def insert(self, node):
      if node.key <= self.key: 
         # self.left = node
         # node.parent = self
         if self.left == None:
            self.left = node
            node.parent = self
         else: 
            self.left.insert(node)
      if node.key > self.key: 
         if self.right == None:
            self.right = node
            node.parent = self 
         else: 
            self.right.insert(node)
      # elif node.key >= self.key: 
      #    self.right = node
      #    return

   def search(self, value):
      if value == self.key:
         return self 
      if self.key > value and self.left != None: 
         return self.left.search(value)
      elif self.right != None: 
         return self.right.search(value)
      
      return None

   def delete(self, value): 
      if self.key == value: 
         return None
      if self.left != None and self.left.key == value: 
         self.left = None
         return self
      if self.right != None and self.right.key == value: 
         self.right = None
         return self
      return self 

