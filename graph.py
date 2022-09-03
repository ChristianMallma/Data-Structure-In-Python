class Vertex:
  def __init__(self, identifier) -> None:
    self.identifier = identifier
    self.connections = dict()
  
  def add_neighbor(self, identifier, weight=0):
    self.connections[identifier] = weight
  
  def show_connections(self):
    return self.connections.keys()
  
  def show_identifier(self):
    return self.identifier
  
  def show_weight(self, identifier):
    return self.connections[identifier]
  
  def __str__(self) -> str:
    return str(self.identifier) + " connect with " + str([c for c in self.connections])


class Graph:
  def __init__(self) -> None:
    self.vertexs = dict()
    self.number_of_vertexs = 0
  
  def add_new_vertex(self, identifier):
    new_vertex = Vertex(identifier)
    self.vertexs[identifier] = new_vertex
    self.number_of_vertexs += 1
    return new_vertex
  
  def show_vertex(self, identifier):
    if identifier in self.vertexs:
      return self.vertexs[identifier]
    else:
      return None
  
  def add_edge(self, origin, destiny, weight=0): #edge => arista
    if origin not in self.vertexs:
      self.add_new_vertex(origin)
    if destiny not in self.vertexs:
      self.add_new_vertex(destiny)
    
    self.vertexs[origin].add_neighbor(destiny, weight)
  
  def show_vertex_list(self):
    return self.vertexs.keys()
  
  def __iter__(self):
    return iter(self.vertexs.values())


# Test
# vertex = Vertex(5)
# print(vertex.show_identifier())

graph = Graph()
graph.add_new_vertex(1)
graph.add_new_vertex(2)
graph.add_new_vertex(3)
graph.add_new_vertex(4)

print(graph.show_vertex_list())

graph.add_edge(1,2,4)
graph.add_edge(1,4,2)
graph.add_edge(2,4,1)
graph.add_edge(2,3,1)

for vertex in graph:
  print(vertex)