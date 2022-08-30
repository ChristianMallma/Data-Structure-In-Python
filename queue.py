class Queue:
  def __init__(self) -> None:
    self.elements = []
  
  def is_empty(self):
    return self.elements == []
  
  def insert(self, element):
    self.elements.insert(0, element)
  
  def delete(self):
    if len(self.elements) == 0:
      raise ValueError("Can't delete elements. The list is empty")
    self.elements.pop()
  
  def size_of_queue(self):
    return len(self.elements)
  
  def show_elements(self):
    return self.elements

# Test
queue = Queue()

# Insert elements
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
print(queue.show_elements())

# Size
print(queue.size_of_queue())

# Delete element
queue.delete()
print(queue.show_elements())

queue.delete()
queue.delete()
queue.delete()
print(queue.is_empty())
# queue.delete()
