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

        # Intentionally commented the lines
        # node = AdjNode(source)
        # node.next = self.graph[destination]
        # self.graph[destination] = node

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


def find_all_paths_recursive(graph, source, destination, visited, path, paths):
    """
    Finds all paths between source and destination in given graph
    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    :param visited: A list to mark visited vertices
    :param path: List to store one path to source from destination
    :param paths: 2D list to store all paths
    """

    # Mark the current node as visited and store in path
    visited[source] = True
    path.append(source)

    # If current vertex is same as destination, then print
    # stores the current path in 2D list (Deep copy)
    if source == destination:
        paths.append(copy.deepcopy(path))
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        while graph.graph[source] is not None:
            i = graph.graph[source].vertex

            if not visited[i]:
                find_all_paths_recursive(graph, i, destination, visited, path, paths)

            graph.graph[source] = graph.graph[source].next

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[source] = False


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    temp = graph.graph[start]
    while temp:
        if temp.vertex not in visited:
            dfs(graph, temp.vertex, visited)
        temp = temp.next
    return visited

def transpose(graph):
    graph_t = Graph(graph.V)
    for v in range(graph.V):
        temp = graph.graph[v]
        while temp:
            graph_t.add_edge(temp.vertex, v)
            temp = temp.next
    return graph_t

def is_strongly_connected(graph):
    """
    Finds if the graph is strongly connected or not
    :param graph: The graph
    :return: returns True if the graph is strongly connected, otherwise False
    """

    # Step 1: Do DFS traversal starting from the first vertex.
    result = dfs(graph, 0)

    # If DFS traversal doesn't visit all vertices, then return false
    if graph.V != len(result):
        return False

    # Step 2: Create a reversed graph
    graph2 = transpose(graph)

    # Step 3: Do DFS for reversed graph starting from the first vertex.
    # Staring Vertex must be same starting point of first DFS
    result = dfs(graph2, 0)

    # If all vertices are not visited in second DFS, then
    # return false
    if graph2.V != len(result):
        return False

    return True


# Main program to test the above code
if __name__ == "__main__":

    V = 5
    g1 = Graph(V)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(3, 0)
    g1.add_edge(4, 2)
    print("Yes" if is_strongly_connected(g1) else "No")

    g2 = Graph(V)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(2, 4)
    print ("Yes" if is_strongly_connected(g2) else "No")