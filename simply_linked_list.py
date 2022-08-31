class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.next_node = None

# Creating nodes
node1 = Node("one")
node2 = Node("two")
node3 = Node("three")

# Linking
node1.next_node = node2
node2.next_node = node3

# Test
print(node1.value)
print(node1.next_node)
print(node1.next_node.value)
print(node2.value)