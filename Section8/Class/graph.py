class GraphNode:
    def __init__(self, data):
        self.neighbors = []
        self.data = data

    def dfs_rec(self, visited):
        if self.data not in visited:
            visited.append(self.data)
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

    def add_edge(self, source, target):
        if source not in self.nodes or target not in self.nodes:
            return False

        self.nodes[source].add_neighbor(self.nodes[target])
        return True

    def dfs(self, node):
        visited = self.nodes[node].dfs_rec([])
        print(visited)


if __name__ == "__main__":
    graph = Graph()

    for i in range(20):
        graph.add_node(i)

    for i in range(20):
        graph.add_edge(i, i + 1 % 20)

    graph.dfs(17)




