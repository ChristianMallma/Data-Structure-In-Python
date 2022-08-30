class Deque:
  def __init__(self) -> None:
    self.elements = []
  
  def insert_at_start(self, element):
    self.elements.insert(0, element)
  
  def insert_at_end(self, element):
    self.elements.append(element)
  
  def delete_at_start(self):
    if len(self.elements) == 0:
      raise ValueError("Can't delete elements. The list is empty")
    self.elements.pop(0)
  
  def delete_at_end(self):
    if len(self.elements) == 0:
      raise ValueError("Can't delete elements. The list is empty")
    self.elements.pop()
  
  def size_of_deque(self):
    return len(self.elements)
  
  def show_elements(self):
    return self.elements
  
  def is_empty(self):
    return self.elements == []

# Test
deque = Deque()

# Insert elements
deque.insert_at_start(1)
deque.insert_at_end(2)
deque.insert_at_end(3)
deque.insert_at_end(4)

# Show elements
print(deque.show_elements())

# Delete
deque.delete_at_start()
print(deque.show_elements())

deque.delete_at_end()
print(deque.show_elements())