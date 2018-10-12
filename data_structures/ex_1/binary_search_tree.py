import sys

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.children = []

  def get_rev_children(self):
    children = self.children[:]
    children.reverse()
    return children

  def get_children(self):
    return self.children

  def depth_first_for_each(self, cb):
    nodes = []
    stack = [self]
    while stack:
      curr_node = stack[0]
      stack = stack[1:]
      nodes.append(curr_node)
      cb(curr_node.value)
      for child in curr_node.get_rev_children():
        stack.insert(0, child)
    return nodes

  def breadth_first_for_each(self, cb):
    nodes = []
    stack = [self]
    while stack:
      curr_node = stack[0]
      stack = stack[1:]
      nodes.append(curr_node)
      cb(curr_node.value)
      for child in curr_node.get_children():
        stack.append(child)
    return nodes

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
        self.children.append(new_tree)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
        self.children.append(new_tree)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
