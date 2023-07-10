from graphviz import Digraph, Graph as GraphV


class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []


class Graph:
    def __init__(self, matrix):
        self.nodes = []
        for i in range(len(matrix)):
            self.nodes.append(Node(i))

        for i in range(len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 1:
                    if i != j:
                        self.nodes[i].neighbors.append(self.nodes[j])

    def draw_graph(self):
        g = Digraph(engine='circo')
        for node in self.nodes:
            g.attr('node', style='filled', fillcolor='white', fontcolor='black', shape='circle')
            g.node('%i' % node.id, '%i' % node.id)

        handled = [[]]
        for node in self.nodes:
            for neighbor in node.neighbors:
                handled.append([node, neighbor])
                g.edge('%i' % node.id, '%i' % neighbor.id)

        g.view(filename="graph")

    @staticmethod
    def draw_graph_from_list(adj_list):
        g = GraphV(engine="circo")
        g.attr('node', fillcolor='black', fontcolor='white', shape='rectangle', style='filled', border='black')
        for name in adj:
            g.node(name, name)
        edges = set()
        for name in adj:
            for dom, dist in adj[name]:
                if (str(dom), str(name), str(dist)) in edges:
                    continue
                g.edge(str(name), str(dom), str(dist))
                edges.add((str(name), str(dom), str(dist)))

        g.view(filename="list")

    @staticmethod
    def draw_graph_from_mat(matrix):
        if Graph.matrix_symmetric(matrix):
            g = GraphV(engine="circo")
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
                    if isinstance(g, GraphV):
                        if (str(j), str(i)) in edges:
                            continue
                        edges.add((str(i), str(j)))
                    g.edge(str(i), str(j), str(matrix[i][j]))
        g.render(filename="g_mat", format="png")

    @staticmethod
    def matrix_symmetric(matrix):
        symmetric = True
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != matrix[j][i]:
                    symmetric = False
        return symmetric


if __name__ == '__main__':
    matrix = [[0, 1, 1, 1],
              [1, 0, 1, 1],
              [1, 1, 0, 1],
              [1, 1, 1, 0]]
    # Graph.draw_graph_from_mat(matrix)
    # g = Graph(matrix)
    # g.draw_graph()
    adj = {'yahoo.com': [('facebook.com', 2), ('twitter.com', 2), ('google.com', 3)],
           'google.com': [('instagram.com', 1), ('LordVoldemodem', 1), ('yahoo.com', 3), ('twitter.com', 3),
                    ('facebook.com', 5), ('reddit.com', 5)],
           'facebook.com': [('twitter.com', 1), ('yahoo.com', 2), ('google.com', 5)],
           'twitter.com': [('instagram.com', 1), ('facebook.com', 1), ('yahoo.com', 2), ('google.com', 3)],
           'instagram.com': [('google.com', 1), ('reddit.com', 1), ('twitter.com', 1)],
           'reddit.com': [('instagram.com', 1), ('google.com', 5)], 'LordVoldemodem': [('google.com', 1)],
           'DesktopD': [('Mobile1', 1), ('DesktopC', 3)], 'DesktopC': [('Modem', 1), ('Mobile1', 2), ('DesktopD', 3)],
           'Mobile1': [('DesktopD', 1), ('DesktopC', 2)], 'Modem': [('DesktopC', 1)]
           }
    Graph.draw_graph_from_list(adj)




