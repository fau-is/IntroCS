from graphviz import Digraph

class Graph(dict)
    def __init__():
        super().__init__()

    def add_node(n):
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
                


    def bfs()





