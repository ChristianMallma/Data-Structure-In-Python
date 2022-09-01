from curses import noecho


class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.left_branch = None
    self.right_branch = None

class BinaryTree:
  def __init__(self, value) -> None:
    self.root = Node(value)
  
  # Private functions
  def __insert_recursive(self, node: Node, value):
    if value < node.value:
      if node.left_branch is None:
        node.left_branch = Node(value)
      else:
        self.__insert_recursive(node.left_branch, value)
    else:
      if node.right_branch is None:
        node.right_branch = Node(value)
      else:
        self.__insert_recursive(node.right_branch, value)
  
  def __inorden_recursive(self, node: Node):
    if node is not None:
      self.__inorden_recursive(node.left_branch) # left visit
      print(node.value, end=', ') # current visit
      self.__inorden_recursive(node.right_branch) # right visit
  
  def __preorden_recursive(self, node: Node):
    if node is not None:
      print(node.value, end=', ') # current visit
      self.__preorden_recursive(node.left_branch) # left visit
      self.__preorden_recursive(node.right_branch) # right visit
  
  def __postorden_recursive(self, node: Node):
    if node is not None:
      self.__postorden_recursive(node.left_branch) # left visit
      self.__postorden_recursive(node.right_branch) # right visit
      print(node.value, end=', ') # current visit
  
  def __find_node(self, node: Node, value):
    if node is None:
      return False
    if value == node.value:
      print('line 49')
      return True
    if value < node.value:
      return self.__find_node(node.left_branch, value)
    else:
      return self.__find_node(node.right_branch, value)
  
  # Public functions
  def insert_value(self, value):
    self.__insert_recursive(self.root, value)
  
  def inorden(self):
    self.__inorden_recursive(self.root)
  
  def preorden(self):
    self.__preorden_recursive(self.root)
  
  def postorden(self):
    self.__postorden_recursive(self.root)
  
  def find_value(self, value):
    return self.__find_node(self.root, value)


# Test
b_t = BinaryTree(45)
b_t.insert_value(23)
b_t.insert_value(2)
b_t.insert_value(65)
b_t.insert_value(38)
b_t.insert_value(52)
b_t.insert_value(96)
b_t.insert_value(7)
b_t.insert_value(48)

print('Inorden')
b_t.inorden()
print()

print('Preorden')
b_t.preorden()
print()

print('Postorden')
b_t.postorden()
print()

result = b_t.find_value(38)
print(result)
