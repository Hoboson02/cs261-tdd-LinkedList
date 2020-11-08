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
      if node.key <= self.key and self.left == None: 
         self.left = node
         node.parent = self
      elif node.key >= self.key: 
         self.right = node
         return

   def search(self, value):
      if value == self.key:
         return self 
      else: 
         return None
