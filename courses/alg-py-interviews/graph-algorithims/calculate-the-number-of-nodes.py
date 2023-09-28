def number_of_nodes(graph, level):
    """
    Calculates the number of nodes at given level
    :param graph: The graph
    :return: Total number of nodes at given level
    """

    # Write your code here!
    source = 0

    visited = [0] * len(graph.graph)

    queue = []

    queue.append(source)
    visited[source] = 1

    while queue:
        source = queue.pop(0)

        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if visited[data] == 0:
                queue.append(data)
                visited[data] = visited[source] + 1
            graph.graph[source] = graph.graph[source].next

    result = 0
    for i in range(len(graph.graph)):
        if visited[i] == level:
            result += 1
    return result
