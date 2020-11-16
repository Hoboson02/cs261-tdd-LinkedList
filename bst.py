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
      if self.key == value:
         return self 
      if self.key > value and self.left != None: 
         return self.left.search(value)
      elif self.right != None: 
         return self.right.search(value)
      
      return None

   def has_left_child(self):
      return not (self.left is None)  

   def has_right_child(self):
      return not (self.right is None)  

   def is_leaf(self): 
      return not (self.has_left_child() or self.has_right_child())

   def minimum(self): 
      if self.left == None: 
         return self
      else: 
         return self.left.minimum() 

   def delete(self, value): 
      if value < self.key: 
         if self.has_left_child(): 
            self.left = self.left.delete(value)
         return self 
      elif value > self.key: 
         if self.has_right_child(): 
            self.right = self.right.delete(value)
         return self 

      elif value == self.key: 
         if self.is_leaf(): 
            return None
         elif self.has_left_child() and not self.has_right_child(): 
            return self.left
         elif self.has_right_child() and not self.has_left_child(): 
            return self.right
         else: 
            new_root = self.right.minimum() 
            new_root.right = self.right.delete(new_root.key)
            new_root.left = self.left 
            return new_root

   def keys(self, order):
      keylist = []
      if order == 'pre' or 'in' or 'post': 
         keylist.append(self.key)
         if self.left != None: 
            self.left.keys(order)
         elif self.right != None: 
            self.right.keys(order)
         return keylist
      # elif order == 'in': 
      #    keylist.append(self.key)
      #    if self.left != None: 
      #       self.left.keys(order)
      #    elif self.right != None: 
      #       self.right.keys(order)
      #    return keylist
      # elif order == 'post': 
      #    keylist.append(self.key)
      #    if self.left != None: 
      #       self.left.keys(order)
      #    elif self.right != None: 
      #       self.right.keys(order)
      #    return keylist



      # if self.left != None and self.left.key == value: 
      #    self.left = self
      #    return self
      # if self.right != None and self.right.key == value: 
      #    self.right = self
      #    return self
      # return self 

   

   

