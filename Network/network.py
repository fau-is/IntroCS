class Graph(dict):
    def __init__(self):
        super().__init__()

    def add_vertex(self, key):
        # TODO

    def add_edge(self, origin, target, weight):
        # TODO

    def dfs(self, start, vertex_list=[]):
        # TODO

    def bfs(self, start):
        # TODO

    def dijkstra(self, start, end):
        # TODO


g = Graph()
edges = ['AB3', 'AE2', 'AF2', 'BA3', 'BE3', 'BF5', 'BD1', 'BC5', 'CB5', \
         'CD1', 'DC1', 'DB1', 'DE1', 'EB3', 'EA2', 'EF1', 'FA2', 'FB5', 'FE1', 'ZY1', 'YX3']
for edge in edges:
    g.add_edge(edge[:1], edge[1], int(edge[2:]))

print(g)
print(g.dfs('A'))
print(g.bfs('A'))
g.dijkstra('A', 'D')
print(g.bfs('Y'))
