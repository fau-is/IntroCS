from graph_exercises import Graph
import sys
import graphviz
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

if __name__ == '__main__':



    g = Graph()
    # Edges = [('yahoo.com', 'google.com', 3), ('yahoo.com', 'facebook.com', 2), ('yahoo.com', 'twitter.com', 2),
    #          ('google.com', 'facebook.com', 5), ('google.com', 'twitter.com', 3), \
    #          ('google.com', 'instagram.com', 1), ('google.com', 'reddit.com', 5), ('LordVoldemodem', 'google.com', 1),
    #          ('reddit.com', 'instagram.com', 1), ('instagram.com', 'twitter.com', 1), \
    #          ('twitter.com', 'facebook.com', 1), ('DesktopD', 'DesktopC', 3), ('DesktopD', 'Mobile1', 1),
    #          ('Mobile1', 'DesktopC', 2), ('DesktopC', 'Modem', 1)]
    Edges = [('Marissa', 'Sundar', 3), ('Marissa', 'Mark', 2), ('Marissa', 'Elon', 2),
             ('Sundar', 'Mark', 5), ('Sundar', 'Elon', 3), \
             ('Sundar', 'Adam', 1), ('Sundar', 'Jack', 5), ('Tim', 'Sundar', 1),
             ('Jack', 'Adam', 1), ('Adam', 'Elon', 1), \
             ('Elon', 'Mark', 1), ('Olaf', 'Emanuel', 3), ('Olaf', 'Rishi', 1),
             ('Rishi', 'Emanuel', 2), ('Emanuel', 'Joe', 1)]

    for edge in Edges:
        a, b, c = edge
        g.add_edge(a, b, c)
    print(g)
    print(g.dfs('Marissa'))
    print(g.bfs('Elon'))
    a, b = g.dijkstra('Marissa', 'Jack')
    print('Shortest distance is ' + str(a))
    print('Path: ' + str(b))
    print(g.bfs('Rishi'))

    print_graph(g)
    print()

    # ------------ Mastodon (unweighted) User Network --------------

    # TODO: Find the most influential user based on the amount of followers (edges branching off)
    #       - Distinguish edge direction between followers and people the person follows?

    g.most_influential_1()

    # TODO: Find the most influential user based on "betweenness"
    #       (Number of shortest paths (dijkstra) from all nodes to all others that pass through a particular node)
    #       In case of unweighted graph (which is likely) BFS should find shortest path

    g.most_influential_2()

    # TODO: Find the most influential user based on „Closeness“
    #       average length of the shortest paths (dijkstra) between a specific node and all other nodes in the graph)
    #       In case of unweighted graph (which is likely) BFS should find shortest path
    #       example: Variant can answer the question "On average, through how many corners are you connected to every other person in the network?

    g.most_influential_3()

    # ------------ Mastodon (weighted) Status Network --------------
    print()
    s = Graph()

    Mentions = [('TBT', 'MondayMotivation', 300), ('TBT', 'OOTD', 200), ('TBT', 'Love', 200),
             ('MondayMotivation', 'OOTD', 500), ('MondayMotivation', 'Love', 300), \
             ('MondayMotivation', 'Travel', 100), ('MondayMotivation', 'Foodie', 500), ('Fitness', 'MondayMotivation', 100),
             ('Foodie', 'Travel', 100), ('Travel', 'Love', 100), \
             ('Love', 'OOTD', 100), ('Funny', 'Selfie', 300), ('Funny', 'Music', 100),
             ('Music', 'Selfie', 200), ('Selfie', 'Politics', 100)]
    for edge in Mentions:
        a, b, c = edge
        s.add_edge(a, b, c)

    print_graph(s)

    # TODO: Implement task to identify
    #       - most popular tag pair (highest edge weight)
    #       - tag that appears with the most other tags (amount of edges branching off)

    # TODO: Implement DFS/BFS exercise that filters out pairs that have been tweeted at least 100 times