from node import Node


class Graph:
    """"
    A class to create and manipulate an undirect graph
    """
    def __init__(self):
        self.adj_list = {}
        self.size = 0

    def add_vertex(self, value):
        """"
        A method to add a vertex to the adjacency list
        """
        new_vertex = Node(value)

        self.adj_list[new_vertex] = []
        self.size+=1

        return new_vertex
    
    def add_edge(self,vertex1, vertex2):

        """"
        A method to add an edge between two vertices
        """

        if vertex1 not in self.adj_list.keys():
            return("this vertex does not exist")
        
        if vertex2 not in self.adj_list.keys():
            return("this vertex does not exist")
        
        
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

    def get_vertices(self):
      """
      A method to get all vertices in the adjacency list
      """
      if self.size ==0 :
          return "Empty adjacency list"
      
      output = ""
        
      for vertex in self.adj_list.keys():
            output += " " + vertex.value + " --->"

      return output
    
    def get_neighbors(self,vertex):
        """
        A method to get all neighbors for the given vertex
        """
        if vertex not in self.adj_list.keys():
            return "The vertex not in the adjacency list"
        
        output = ""
        
        for neighbor in self.adj_list[vertex]:
            output += " " + neighbor.value + " --->"
        
        return output

    def get_size(self):
        """
        A method to get the size of the adjacency list which is the total number of the vertices
        """
        if self.size == 0:
            return None
        
        return self.size
    
    def __str__(self):
        """
        A wrapper to see the graph
        """
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge} -----> '
            output += '\n'
        return output


graph1 = Graph()

a = graph1.add_vertex("A")
b = graph1.add_vertex("B")
c = graph1.add_vertex("C")
d = graph1.add_vertex("D")

graph1.add_edge(a,b)
graph1.add_edge(a,c)
graph1.add_edge(c,b)
graph1.add_edge(d,b)
graph1.add_edge(d,c)

# print(graph1)
# print(graph1.get_size())
# print(graph1.get_neighbors(a))
# print(a)

print(graph1.get_vertices())
        



