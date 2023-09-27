
# solution with a queue
def bfs(graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """    
    # Mark all the vertices as not visited
    visited = [False] * (len(graph.graph))

    # Create a queue for BFS
    queue = []

    # Result string
    result = ""

    # Mark the source node as
    # visited and enqueue it
    queue.append(source)
    visited[source] = True
    

    while queue:

        # Dequeue a vertex from
        # queue and print it
        source = queue.pop(0)
        result += str(source)

        temp=graph.graph[source] # original graph will not be affected

        # Get all adjacent vertices of the
        # dequeued vertex source. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        while temp is not None:
            data = temp.vertex
            if not visited[data]:
                queue.append(data)
                visited[data] = True
            temp=temp.next

    return result




# graph Initialization

class AdjNode:
    """
    A class to represent the adjacency list of the node
    """

    def __init__(self, data):
        """
        Constructor
        :param data : vertex
        """
        self.vertex = data
        self.next = None


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, vertices):
        """
        Constructor
        :param vertices : Total vertices in a graph
        """
        self.V = vertices
        self.graph = [None] * self.V


    def add_edge(self, source, destination):
        """
        add edge
        :param source: Source Vertex
        :param destination: Destination Vertex
        """

        # Adding the node to the source node
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        # Adding the source node to the destination if undirected graph
        
        # Intentionally commented the lines
        #node = AdjNode(source)
        #node.next = self.graph[destination]
        #self.graph[destination] = node

    def print_graph(self):
        """
        A function to print a graph
        """
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")