class GraphNode:
    def __init__(self, data):
        self.neighbors = []
        self.data = data

    def dfs_rec(self, visited):
        if self not in visited:
            visited.append(self)
            for neighbor in self.neighbors:
                visited = neighbor.dfs_rec(visited)
        return visited

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

class Graph():
    def __init__(self):
        self.nodes = {}
        self.adj_matrix = {}

    def add_node(self, data):
        g_node = GraphNode(data)
        self.nodes[data] = g_node
        self.adj_matrix[data] = []

    def add_edge(self, source, target):
        if source not in adj_matrix or target not in adj_matrix:
            return False

        


