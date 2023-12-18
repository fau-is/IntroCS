from graph_drawer import Graph as GraphDrawer

class Graph(dict):
    def __init__(self):
        super().__init__()

    def add_node(self, n):
        self[n] = []

    def add_edge(self, a: str, b: str):
        if a not in self:
            self.add_node(a)

        self[a].append(b)
        self[a] = sorted(self[a])


    def dfs(self, s: str):
        if s not in self:
            raise ValueError("Node does not exist")

        stack = [s]
        visited = []

        while stack:
            node = stack.pop()
            visited.append(node)
            for neighbor in self[node]:
                stack.append(neighbor)
            print(node)

    def bfs(self):
        pass

if __name__ == "__main__":
    g = Graph()

    g.add_edge("a", "b")
    g.add_edge("a", "c")
    g.add_edge("b", "d")
    g.add_edge("d", "e")

    g.dfs("a")

    GraphDrawer.draw_graph_from_list(self)







