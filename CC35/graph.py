from vertex import Vertex
from Queue import Queue

class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

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
        new_vertex = Vertex(value)

        self.adj_list[new_vertex] = []
        self.size+=1

        return new_vertex
    
    def add_edge(self,vertex1, vertex2,weight=0):

        """"
        A method to add an edge between two vertices
        """

        if vertex1 not in self.adj_list.keys():
            return("this vertex does not exist")
        
        if vertex2 not in self.adj_list.keys():
            return("this vertex does not exist")
        
        
        edge1_2 = Edge(vertex1,weight)
        edge2_1 = Edge(vertex2,weight)

        self.adj_list[vertex1].append(edge2_1)
        self.adj_list[vertex2].append(edge1_2)

    def get_vertices(self):
      """
      A method to get all vertices in the adjacency list
      """
      if self.size ==0 :
          return "Empty adjacency list"
      
      output = ""
        
      for vertex in self.adj_list.keys():
            output += " " + vertex.value + " --->"

      return list(self.adj_list.keys())
    
    def get_neighbors(self,vertex):
        """
        A method to get all neighbors for the given vertex
        """
        if vertex not in self.adj_list.keys():
            return "The vertex not in the adjacency list"
        
        lis = []
        
        for neighbor in self.adj_list[vertex]:
            lis.append(neighbor)
        
        return lis

    def get_size(self):
        """
        A method to get the size of the adjacency list which is the total number of the vertices
        """
        if self.size == 0:
            return None
        
        return self.size
    
    def breadth_first(self, root_vertex):
        """
        A method to traverse the graph using breadth_first way which will traverse it level by level
        """
        nodes = []
        breadth = Queue()
        visited = set()

        breadth.enqueue(root_vertex)
        visited.add(root_vertex)

        while not breadth.isEmpty():
            front = breadth.dequeue()
            nodes.append(front)

            for edge in self.get_neighbors(front):
                child = edge.vertex
                if child not in visited:
                    visited.add(child)
                    breadth.enqueue(child)

        output =""
        for node in nodes :
            output += " " + node.value

        return output
    



    
    def __str__(self):
        """
        A wrapper to see the graph
        """
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output

def business_trip(graph, cities):
            """"
            A function to calculate the total cost for a trip(graph) passing by cities(vertices)
            """
            cost = 0
            for i in range(len(cities) - 1):
                curr = cities[i]
                nxt = cities[i + 1]

            

                for vertex in graph.get_vertices() : 
                    if vertex.value == curr:

                
                        for edge in graph.adj_list[vertex]:
                            if edge.vertex.value == nxt:
                                cost += edge.weight
                                break

            if cost == 0  :
                return None
            
            return "$" + str(cost)
    


graph1 = Graph()

# a = graph1.add_vertex("A")
# b = graph1.add_vertex("B")
# c = graph1.add_vertex("C")
# d = graph1.add_vertex("D")

# graph1.add_edge(a,b)
# graph1.add_edge(a,c)
# graph1.add_edge(c,b)
# graph1.add_edge(d,b)
# graph1.add_edge(d,c)

a = graph1.add_vertex("Pandora")
b = graph1.add_vertex("Arendelle")
c = graph1.add_vertex("Metroville")
d = graph1.add_vertex("Monstropolis")
e = graph1.add_vertex("Narnia")
f = graph1.add_vertex("Naboo")

graph1.add_edge(a,b,150)
graph1.add_edge(a,c,82)
graph1.add_edge(b,c,99)
graph1.add_edge(b,d,42)
graph1.add_edge(c,d,105)
graph1.add_edge(c,e,37)
graph1.add_edge(d,f,73)
graph1.add_edge(c,f,26)
graph1.add_edge(e,f,250)


# print(graph1)
# print(graph1.get_size())
# print(graph1.get_neighbors(a))
# print(a)

# print(graph1.get_vertices())

# print(graph1.breadth_first(a))

print(business_trip(graph1,["Arendelle","Monstropolis", "Naboo"]))
        



