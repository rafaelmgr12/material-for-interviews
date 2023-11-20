import copy


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
        node = AdjNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

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
            
            
def connected_components(graph):
    """
    Function to find the connected components
    :param graph: The graph
    :return: returns a list of connected components
    """
    visited = []
    result = []
    
    for i in range(graph.V):
        visited.append(False)
    for v in range(graph.V):
        if not visited[v]:
            result.append(dfs(graph, v, visited))
    return result


# Helper Function of DFS. Might be useful
def dfs(g, source, visited):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a list
    """
 

    graph = copy.deepcopy(g)

    # Create a stack for DFS
    stack = []

    # Result list
    result = []

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack[-1]
        stack.pop()

        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next

    return result

# Main program to test above function
if __name__ == "__main__":

    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    result = connected_components(g)

    print("Following are connected components")
    print(result)