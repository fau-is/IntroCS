from solutions.graph_sol import Graph
import graphviz
import os

def print_banner(text: str, symbol: str = "="):
    print(symbol * len(text))
    print(text)
    print(symbol * len(text))

# ---- Main Script Starts Here ----
if __name__ == "__main__":

    print_banner("IntroCS: Graphs - Social Network Analysis applied to Mastodon data")

    # ---- Exercise 1.1: Implement Graph and User class, then visualize network ----
    print_banner("Exercise 1.1: Graph implementation", "-")

    g = Graph()
    print("Parsing real-world data from Mastodon API...")
    g.parse_data()

    print("Creating network visualization...")
    g.show()
    print("Network visualization created and stored as a PNG file.\n")


    # ---- Exercise 1.2: Check connectivity of graph ----
    print_banner("Exercise 1.2: Network Connectivity (DFS)", "-")

    subgraphs = g.get_subgraphs()
    status = "connected" if len(subgraphs) == 1 else "disconnected"
    print(f"Our {status} network consists of {len(subgraphs)} {status} {'subgraph' if len(subgraphs) == 1 else 'subgraphs'}.\n")


    # ---- Exercise 1.3: Find the shortest path connecting two users ----
    print_banner("Exercise 1.3: Shortest Path (BFS with path tracking)", "-")

    user1, user2 = "Gritche", "rysiek"
    shortest_path = g.shortest_path(user1, user2)

    if shortest_path:
        print(f"The shortest_path between {user1} and {user2} is {shortest_path}.\n")
    else:
        print(f"There exists no connection between {user1} and {user2}.\n")


    # ---- Exercise 1.4: Find the most influential user ----
    print_banner("Exercise 1.4: Most Influential User (Closeness)", "-")

    mip, min_avg_length = g.most_influential()
    print(f"{mip} is the most influential person in the network with an avg shortest path length of {min_avg_length} to all other users.\n")
    # Optionally: let self.most_influential() print out the average length of all average shortest path lengths.

    # ---- Exercise 1.5: Detect communities within the network ----
    print_banner("Exercise 1.5: Community Detection (Girvan Newman Algorithm)", "-")

    # Remove already existing clusters of single users
    remove = [i[0] for i in g.get_subgraphs() if len(i) == 1]
    for user in remove:
        g.remove_vertex(user)

    n = 2
    communities = g.girvan_newman_algorithm(clusters=n)
    print(f"For n = {n} clusters, the Girvan Newman algorithm detected the following communities:")
    for i, c in enumerate(communities, 1):
        print(f"\tCommunity {i} - {c}")

    print("Creating final visualization with identified communities...")
    g.show()
    print("Visualization updated and stored as a PNG file.\n")

    print_banner("End of Problem Set")
