import sys
sys.path.append('/Users/chris/christian/developer/Data-Structures-In-Python')

from circular_list import Node

def circular(node):
    pointer1 = node
    pointer2 = node
    while pointer2 != None and pointer2.next_node != None:
      pointer1 = pointer1.next_node
      pointer2 = pointer2.next_node.next_node
      if pointer1 == pointer2:
        return True
    return False


# Test
node1 = Node('one')
node2 = Node('two')
node3 = Node('three')

node1.next_node = node2
node2.next_node = node3
node3.next_node = node1

print(circular(node1))



