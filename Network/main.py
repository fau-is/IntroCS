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
Edges = [('yahoo.com', 'google.com', 3), ('yahoo.com', 'facebook.com', 2), ('yahoo.com', 'twitter.com', 2), ('google.com', 'facebook.com', 5), ('google.com', 'twitter.com', 3), \
        ('google.com', 'instagram.com', 1), ('google.com', 'reddit.com', 5), ('LordVoldemodem', 'google.com', 1), ('reddit.com', 'instagram.com', 1), ('instagram.com', 'twitter.com', 1), \
        ('twitter.com', 'facebook.com', 1), ('DesktopD', 'DesktopC', 3), ('DesktopD', 'Mobile1', 1), ('Mobile1', 'DesktopC', 2), ('DesktopC', 'Modem', 1)]

for edge in Edges:
    a, b, c = edge
    g.add_edge(a, b, c)

print(g)
print(g.dfs('yahoo.com'))
print(g.bfs('twitter.com'))
a, b = g.dijkstra('yahoo.com', 'reddit.com')
print('Shortest distance is ' + str(a))
print('Path: ' + str(b))
print(g.bfs('Mobile1'))