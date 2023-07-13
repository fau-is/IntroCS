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
             ('Rishi', 'Emanuel', 2), ('Emanuel', 'Joe', 1), ('Sundar', "Emanuel",2)]

    for edge in Edges:
        a, b, c = edge
        g.add_edge(a, b, c)
    # print(g)
    # print(g.dfs('Marissa'))
    # print(g.bfs('Elon'))
    # a, b = g.dijkstra('Marissa', 'Jack')
    # print('Shortest distance is ' + str(a))
    # print('Path: ' + str(b))
    # print(g.bfs('Rishi'))
    #
    # print_graph(g)
    # print()

    # ------------ Mastodon (unweighted) User Network --------------

    # 1. Determine if a graph is connected or not using DFS
    if len(g.dfs('Elon')) == len(g):
        print("1. DFS - The graph is connected")
    else:
        print("1. DFS - The graph is disconnected")

    # 2. Find the shortest path via BFS between two users ("degrees of separation")
    # example: Is there an indirect connection between user a and user b, return the connection
    shortest_connection = g.bfs_find('Jack', 'Marissa')
    if shortest_connection:
        print("2. BFS - Yes there exists an indirect connection", shortest_connection)
    else:
        print("2. BFS - No there doesnt exist an indirect connection")

    # 3.1 Find the most influential user based on the amount of followers (edges branching off)
    # - Distinguish edge direction between followers and people the person follows?
    # - Undirected unweighted graph highly appreciated in terms of task complexity

    g.most_influential_1()

    # 3.2 Find the most influential user based on "betweenness"
    # (Number of shortest paths (bfs implementation from above or dijkstra) from all nodes to all others that pass through a particular node)
    # In case of unweighted graph (which is likely) BFS should find shortest path

    g.most_influential_2()

    # 3.3 Find the most influential user based on „Closeness“
    # average length of the shortest paths (bfs implementation from above or dijkstra) between that node and all other nodes in the graph)
    # In case of unweighted graph (which is likely) BFS should find shortest path
    # example: Variant can answer the question "On average, through how many corners are you connected to every other person in the network?

    g.most_influential_3()

    # Todo: 4.1 Cycle detection: DFS can be used to detect cycles in a social network graph.
    #       This could be useful in identifying circular relationships or loops within the network.
    #       Users are nodes and there exist a connection if node a has retweeted a post of person b

    # Todo: 4.2 Community detection via Density measure: BFS can be used to find nodes in close proximity to a specific node.
    #       This can be used to detect communities or groups in a social network.
    #       - Density: This measures the number of existing links over the possible number of links within a group of nodes. A higher density indicates a stronger community
    #
    # 4.3 Community detection via Girvan Newman Algorithm: progressively removing edges with high betweenness centrality
    # from the network, which are considered as "bridges" connecting different communities.
    # Steps:
    #   1. The betweenness of all existing edges in the network is calculated first.
    #   2. The edge(s) with the highest betweenness are removed.
    #   3. The betweenness of all edges affected by the removal is recalculated.
    #   4. Steps 2 and 3 are repeated until no edges remain
    print("4. BFS/Dijkstra Girvan Newman algorithm - Community Detection:")
    communities = g.get_communities(clusters=2)
    for i,c in enumerate(communities):
        print("Community",i,"-",c)
    print_graph(g)

    # ------------ Mastodon (weighted) Status Network --------------
    # TODO: BFS/DFS Use cases for this type of network rather limited, therefore not of priority
    print()
    s = Graph()

    Mentions = [('TBT', 'MondayMotivation', 300), ('TBT', 'OOTD', 200), ('TBT', 'Love', 200),
             ('MondayMotivation', 'OOTD', 600), ('MondayMotivation', 'Love', 300), \
             ('MondayMotivation', 'Travel', 100), ('MondayMotivation', 'Foodie', 500), ('Fitness', 'MondayMotivation', 100),
             ('Foodie', 'Travel', 100), ('Travel', 'Love', 100), \
             ('Love', 'OOTD', 100), ('Funny', 'Selfie', 300), ('Funny', 'Music', 100),
             ('Music', 'Selfie', 200), ('Selfie', 'Politics', 100)]
    for edge in Mentions:
        a, b, c = edge
        s.add_edge(a, b, c)

    # print_graph(s)

    # 1.1 Find most popular tag pair (via highest edge weight)
    print(s.most_popular())

    # 1.2 Find most popular tag pair (via highest edge weight) including a given tag
    print(s.most_popular('Selfie'))

    # 1.3 Find the tag that appears with the most other tags (amount of edges branching off)
    print(s.most_versatile())

    # TODO: Implement DFS/BFS exercise that filters out pairs that have been tweeted at least 100 times

    # TODO: Idea to store together mentioned tags in tree. first level single tags, second level second tag storing tweets with both tags and so on...