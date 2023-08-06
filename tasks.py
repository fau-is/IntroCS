from graph_implementation_unweighted import Graph, print_graph
from tree_implementation import *
import sys
import graphviz
import os


if __name__ == '__main__':

    g = Graph()
    Edges = [('Marissa', 'Sundar'), ('Marissa', 'Mark'), ('Marissa', 'Elon'),
             ('Sundar', 'Mark'), ('Sundar', 'Elon'), \
             ('Sundar', 'Adam'), ('Sundar', 'Jack'), ('Tim', 'Sundar'),
             ('Jack', 'Adam'), ('Adam', 'Elon'), \
             ('Elon', 'Mark'), ('Olaf', 'Emanuel'), ('Olaf', 'Rishi'),
             ('Rishi', 'Emanuel'), ('Emanuel', 'Joe'), ('Sundar', "Emanuel")]

    for edge in Edges:
        a, b = edge
        g.add_edge(a, b)

    print(" ------------ Network: Mastodon (unweighted) User Graph -------------- ")
    print_graph(g)
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
    # print_graph(g)

    # print(" ------------ Mastodon (weighted) Status Network -------------- ")
    # TODO: BFS/DFS Use cases for this type of network rather limited, therefore not of priority
    # print()
    # s = Graph()
    #
    # Mentions = [('TBT', 'MondayMotivation', 300), ('TBT', 'OOTD', 200), ('TBT', 'Love', 200),
    #          ('MondayMotivation', 'OOTD', 600), ('MondayMotivation', 'Love', 300), \
    #          ('MondayMotivation', 'Travel', 100), ('MondayMotivation', 'Foodie', 500), ('Fitness', 'MondayMotivation', 100),
    #          ('Foodie', 'Travel', 100), ('Travel', 'Love', 100), \
    #          ('Love', 'OOTD', 100), ('Funny', 'Selfie', 300), ('Funny', 'Music', 100),
    #          ('Music', 'Selfie', 200), ('Selfie', 'Politics', 100)]
    # for edge in Mentions:
    #     a, b, c = edge
    #     s.add_edge(a, b, c)
    #
    # # print_graph(s)
    #
    # # 1.1 Find most popular tag pair (via highest edge weight)
    # print(s.most_popular())
    #
    # # 1.2 Find most popular tag pair (via highest edge weight) including a given tag
    # print(s.most_popular('Selfie'))
    #
    # # 1.3 Find the tag that appears with the most other tags (amount of edges branching off)
    # print(s.most_versatile())
    #
    # # TODO: Implement DFS/BFS exercise that filters out pairs that have been tweeted at least 100 times
    #
    # # TODO: Idea to store together mentioned tags in tree. first level single tags, second level second tag storing tweets with both tags and so on...

    print(" ------------ Mastodon Followers storing BST ------------------------ ")

    # 1. Fetching Followers
    #  - Fetching followers of a specified id with authentication:
    followers = set()
    access_token = ""
    id = "15530"

    url = f"https://mastodon.social/api/v1/accounts/{id}/followers?limit=80"
    while url:
        response = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})
        objects = json.loads(response.text)  # this converts the json to a python list of dictionary
        usernames = set([i['username'] for i in objects])
        followers |= usernames
        url = response.links['next']['url'] if 'next' in response.links else None


    # 1. Implement a binary search tree class, that stores all the followers of a user alphabetically.
    for user in followers:
        BST.add(user)

    # 2. Implement the recursive binary search algorithm to check wether a username is listed in the user tree.
    # iterative
    # found = BST.find("alextee")
    # if found:
    #     print(found.username, "is among the followers")
    # else:
    #     print("user was not found among the users.")

    # recursive
    found = BST.search(BST.root, "alextee")
    if found:
        print("2. ",found.username, "is among the followers.")
    else:
        print("user was not found among the users.")

    # 3. In order to display all of the followers, use the DFS algorithm from the previous exercise and make slight changes to it, such that it can traverse over the tree in a Pre-, In-, and Postorder.
    print('3. DFS (preorder): ', BST.preorder())
    print_tree(BST.root)
    # TODO: inorder and postorder implementations

    # 4. Implement another suitable data structure of your choice, e.g. hash-table, trie, avl-tree, that beats our BST implementation in terms of search runtime.
    # Parse the followers onto it and compare the runtime for searching using pythons time library.
    to_find = "xolotl"
    # Data structure List: Linear search
    data_list = BST.preorder()
    def linear_search(data, find):
        for user in data:
            if user == find:
                return True
        return False
    exec_time = timeit.repeat(lambda: linear_search(data_list,to_find), number=100)
    print(f"4. user was found using linear search in {sum(exec_time)/len(exec_time)} seconds.")

    # Data structure BST: Binary search
    exec_time = timeit.repeat(lambda:BST.search(BST.root, to_find), number=100)
    print(f"4. user was found using binary search in {sum(exec_time)/len(exec_time)} seconds.")