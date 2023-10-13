import copy  # For deep copy if needed


def find_all_paths(graph, source, destination):
    """
    Finds all paths between source and destination in given graph
    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """

    # Write your code here!
    paths = []

    path = []

    visted = [False] * graph.V

    stack = [(source, path, visted)]

    while stack:
        current, current_path, current_visited = stack.pop()
        current_path = current_path + [current]
        current_visited = current_visited.copy()
        current_visited[current] = True

        if current == destination:
            paths.append(current_path)
        else:
            temp = graph.graph[current]
            while temp:
                if not current_visited[temp.vertex]:
                    stack.append((temp.vertex, current_path, current_visited))
                temp = temp.next

    return paths


## Recursive Solution

def find_all_paths(graph, source, destination):
    """
    Finds all paths between source and destination in given graph
    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """
    # Mark all the vertices as not visited
    visited = [False] * (graph.V)

    # Create a list to store paths
    paths = []
    path = []

    # Call the recursive helper function to find all paths
    find_all_paths_recursive(graph, source, destination, visited, path, paths)
    return paths



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
    
    # Mark the Current node as visisted and sotre in path
    visited[source] = True
    path.append(source)
    
    # If current vertex is same as destination, the print
    # stores the current path in 2D list (deep copy)
    
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
    