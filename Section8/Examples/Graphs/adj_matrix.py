from graphviz import Graph, Digraph

def is_matrix_symmetric(matrix):
    return False


def draw_graph_from_mat(matrix):
    if is_matrix_symmetric(matrix):
        g = Graph(engine="circo")
    else:
        g = Digraph(engine="circo")
    g.attr('node', fillcolor='black', fontcolor='white', shape='rectangle', style='filled', border='black')

    # Create Vertices
    for i in range(len(matrix)):
        g.node(str(i), str(i))

    # Create Edges
    # Set of edges (if symmetric)
    edges = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                if isinstance(g, Graph):
                    if (str(j), str(i)) in edges:
                        continue
                    edges.add((str(i), str(j)))
                g.edge(str(i), str(j), str(matrix[i][j]))
    g.render(filename="g_mat", format="png")


if __name__ == "__main__":
    matrix = [[0, 0, 1, 0],
              [1, 0, 0, 1],
              [0, 1, 0, 0],
              [0, 0, 0, 0]]

    draw_graph_from_mat(matrix)



