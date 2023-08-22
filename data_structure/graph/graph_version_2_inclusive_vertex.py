from collections import deque

class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, to_vertex, weight = 0):
    self.edges[to_vertex] = weight

class Graph:
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = deque([start_vertex])
    seen = set()
    path = {start_vertex: None} # To keep track of the path

    while start:
      current_vertex = start.popleft()
      seen.add(current_vertex)
      print("Visiting " + current_vertex)

      if current_vertex == end_vertex:
        return self._reconstruct_path(path, start_vertex, end_vertex)

      vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
      for vertex in vertices_to_visit:
        if vertex not in seen:
          start.append(vertex)
          path[vertex] = current_vertex

    return False

  def _reconstruct_path(self, path, start_vertex, end_vertex):
    """Helper function to reconstruct the path from start_vertex to end_vertex"""
    current_vertex = end_vertex
    path_to_return = []
    while current_vertex != start_vertex:
      path_to_return.append(current_vertex)
      current_vertex = path[current_vertex]
    path_to_return.append(start_vertex)
    return path_to_return[::-1]
