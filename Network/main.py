import sys
import graphviz
from network import Graph
import os

def print_graph(g):
    graph = graphviz.Graph(format='png', strict=True, filename='network')
    for n in g.keys():
        graph.node(n, n)

    for n in g.keys():
        for t, w in g[n]:
            graph.edge(n, t, label=str(w))
    graph.render()
    os.remove('network')

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
print_graph(g)