class Stack:
  def __init__(self) -> None:
    self.elements = []

  def is_empty(self):
    return self.elements == []
  
  def insert(self, element):
    self.elements.append(element)
  
  def delete(self):
    self.elements.pop()
  
  def find_the_last(self):
    return self.elements[-1]
  
  def size_of_stack(self):
    return len(self.elements)
  
  def show_elements(self):
    return self.elements

# Test
stack = Stack()

# Insert elements
stack.insert("One")
stack.insert("Two")
stack.insert("Three")
stack.insert("Four")
stack.insert("Five")

# Size of the stack
print(stack.size_of_stack())

# Check if is empty
print(stack.is_empty())

# Look the elements
print(stack.show_elements())

# Look last element
print(stack.find_the_last())

# Delete last element
stack.delete()
print(stack.show_elements())