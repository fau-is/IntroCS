from graphviz import Digraph


def print_list_as_graph(adj_list):

    g = Digraph(engine="circo")
    g.attr('node', fillcolor='black', fontcolor='white', shape='rectangle', style='filled', border='black')

    for node in adj_list:
        g.node(str(node), str(node))

    for node in adj_list:
        for connection in adj_list[node]:
            g.edge(str(node), str(connection))

    g.render(filename = "g_list", format="png")

if __name__ == "__main__":


    adj_list = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['A', 'E'],
        'D': ['E'],
        'E': []
    }

    print_list_as_graph(adj_list)

