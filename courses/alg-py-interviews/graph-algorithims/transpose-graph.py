def transpose(graph):
    """
    Transpose the given graph
    :param graph: The graph
    :return: a new transposed graph of the given graph
    """

    new_graph = Graph(graph.V)  # Creating a new graph

    # Write your code here!
    for i in range(graph.V):
       temp = graph.graph[i]
       while temp:
            new_graph.add_edge(temp.vertex, i)
            temp = temp.next    

    return new_graph    
    
    
# Without temp variable
def transpose(my_graph):
    """
    Transpose the given graph
    :param graph: The graph
    :return: a new transposed graph of the given graph
    """

    new_graph = Graph(my_graph.V)  # Creating a new graph

    for source in range(my_graph.V):

        while my_graph.graph[source] is not None:

            destination = my_graph.graph[source].vertex
            # Now the source is destination and vice versa
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next

    return new_graph