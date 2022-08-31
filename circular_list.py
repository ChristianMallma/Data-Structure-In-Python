class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.next_node = None
    self.previous_node = None

# Creating nodes
node1 = Node("one")
node2 = Node("two")
node3 = Node("three")

# Linking
node1.previous_node = node3
node1.next_node = node2

node2.previous_node = node1
node2.next_node = node3

node3.previous_node = node2
node3.next_node = node1

# Test
print(node1.value)
print(node3.next_node.value)
print(node2.previous_node.value)
print(node1.next_node.next_node.value)
print(node3.value)
print(node2.next_node.value)