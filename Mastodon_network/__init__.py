import check50
import check50.py
import json

def import_graph():
    graph_module = check50.py.import_("graph.py")
    if graph_module is None:
        raise check50.Failure("Import failed")
    return graph_module.User, graph_module.Graph

@check50.check()
def exists():
    """graph.py exists"""
    check50.exists("graph.py")

@check50.check(exists)
def username_initialization():
    """User is correctly initialized with username"""
    User, _ = import_graph()
    user = User("Alice")
    if not hasattr(user, 'username'):
        raise check50.Failure("User instance should have an attribute named 'username'.")
    if user.username != "Alice":
        raise check50.Mismatch("Alice", user.username)

@check50.check(username_initialization)
def add_vertex():
    """Vertex added to graph correctly"""
    _, Graph = import_graph()
    graph = Graph()
    graph.add_vertex("Alice")
    if "Alice" not in graph:
        raise check50.Failure("Failed to add vertex 'Alice' to the graph.")

@check50.check(add_vertex)
def add_edge():
    """Edge added to graph correctly"""
    _, Graph = import_graph()
    graph = Graph()
    graph.add_edge("Alice", "Bob")
    if "Bob" not in graph["Alice"]:
        raise check50.Failure("Failed to establish an edge between 'Alice' and 'Bob'.")
    if "Alice" not in graph["Bob"]:
        raise check50.Failure("Failed to establish an edge between 'Bob' and 'Alice'.")

@check50.check(add_edge)
def remove_edge():
    """Edge removed from graph correctly"""
    _, Graph = import_graph()
    graph = Graph()
    graph.add_edge("Alice", "Bob")
    graph.remove_edge(("Alice", "Bob"))
    if "Bob" in graph["Alice"]:
        raise check50.Failure("Failed to remove edge between 'Alice' and 'Bob'.")
    if "Alice" in graph["Bob"]:
        raise check50.Failure("Failed to remove edge between 'Bob' and 'Alice'.")



@check50.check(remove_edge)
def order_ascending():
    """Vertices are in ascending order"""
    _, Graph = import_graph()
    graph = Graph()
    graph.add_edge("Alice", "David")
    graph.add_edge("Alice", "Bob")
    graph.add_edge("Alice", "Charlie")
    if graph["Alice"] != ["Bob", "Charlie", "David"]:
        raise check50.Failure("Neighbors of vertex are not in ascending order.")

def setup_graph_dfs_bfs(Graph):
    graph = Graph()
    user1 = "Alice"
    user2 = "Bob"
    user3 = "Charlie"
    user4 = "David"
    graph.add_edge(user1, user2)
    graph.add_edge(user2, user3)
    graph.add_edge(user3, user4)
    graph.add_edge(user1, user4)
    visited = graph.dfs(user1)
    return graph, visited

def setup_graph_connected(Graph):
    graph = Graph()
    user1 = "Alice"
    user2 = "Bob"
    user3 = "Charlie"
    user4 = "David"
    graph.add_edge(user1, user2)
    graph.add_edge(user2, user3)
    graph.add_edge(user3, user4)
    clusters = graph.get_subgraphs()
    return graph, clusters

def setup_graph_disconnected(Graph):
    graph = Graph()
    user1 = "Alice"
    user2 = "Bob"
    user3 = "Charlie"
    user4 = "David"
    user5 = "Eve"
    user6 = "Frank"
    graph.add_edge(user1, user2)
    graph.add_edge(user3, user4)
    graph.add_edge(user5, user6)
    clusters = graph.get_subgraphs()
    return graph, clusters

def setup_graph(Graph):
    graph = Graph()
    user1 = "Alice"
    user2 = "Bob"
    user3 = "Charlie"
    user4 = "David"
    user5 = "Eve"
    graph.add_edge(user1, user2)
    graph.add_edge(user2, user3)
    graph.add_edge(user3, user4)
    graph.add_edge(user4, user5)
    graph.add_edge(user1, user5)
    path = graph.shortest_path(user1, "David")
    return graph, path


@check50.check(order_ascending)
def dfs_order():
    """Depth-first search returns expected order"""
    _, Graph = import_graph()
    graph, visited = setup_graph_dfs_bfs(Graph)
    if visited != ["Alice", "Bob", "Charlie", "David"]:
        raise check50.Failure("Depth-first search did not return the expected order.")


@check50.check(dfs_order)
def clusters_connected():
    """Graph detects a fully connected cluster correctly"""
    _, Graph = import_graph()
    graph, clusters = setup_graph_connected(Graph)
    if len(clusters) != 1:
        raise check50.Failure("Expected 1 cluster for a fully connected graph.")
    if set(clusters[0]) != {"Alice", "Bob", "Charlie", "David"}:
        raise check50.Failure("Connected cluster doesn't match the expected users.")

@check50.check(clusters_connected)
def clusters_disconnected():
    """Graph detects multiple separated clusters correctly"""
    _, Graph = import_graph()
    graph, clusters = setup_graph_disconnected(Graph)
    if len(clusters) != 3:
        raise check50.Failure("Expected 3 separate clusters for the given graph.")
    for cluster in clusters:
        if len(cluster) not in [2, 2, 2]:
            raise check50.Failure("Each disconnected cluster should have 2 users.")

@check50.check(clusters_disconnected)
def shortest_path_exists():
    """Graph determines shortest path correctly when it exists"""
    _, Graph = import_graph()
    graph, path = setup_graph(Graph)
    if path != ["Alice", "Eve", "David"]:
        raise check50.Failure("Shortest path from 'Alice' to 'David' is incorrect.")

@check50.check(shortest_path_exists)
def no_shortest_path():
    """Graph determines no path exists correctly"""
    _, Graph = import_graph()
    graph, _ = setup_graph(Graph)
    path = graph.shortest_path("Alice", "Frank")
    if path is not None:
        raise check50.Failure("Expected no path between 'Alice' and 'Frank', but a path was returned.")


@check50.check(no_shortest_path)
def shortest_path_direct():
    """Graph determines direct shortest path correctly"""
    _, Graph = import_graph()
    graph, _ = setup_graph(Graph)
    path = graph.shortest_path("Alice", "Eve")
    if path != ["Alice", "Eve"]:
        raise check50.Failure("Shortest path between 'Alice' and 'Eve' is incorrect.")


@check50.check(shortest_path_direct)
def test_most_influential_single_path_one_winner():
    """Most influential user in a modified single path graph correctly identified"""
    _, Graph = import_graph()
    graph = Graph()
    graph.add_edge("Alice", "Bob")
    graph.add_edge("Bob", "Charlie")
    graph.add_edge("Charlie", "David")
    graph.add_edge("Alice", "Charlie")

    influential_users = graph.most_influential()

    # Expect Charlie to be the most influential with a distinct average path length
    expected_winner = "Charlie"
    expected_avg_length = 1.25 

    if len(influential_users) != 1 or influential_users[0][0] != expected_winner or not math.isclose(influential_users[0][1], expected_avg_length, rel_tol=1e-2):
        raise check50.Failure(f"Incorrect most influential user in a modified single path graph.")


@check50.check(test_most_influential_single_path)
def test_most_influential_star_graph():
    """Most influential user in a star graph correctly identified"""
    _, Graph = import_graph()
    graph = Graph()
    graph.add_edge("Center", "Node1")
    graph.add_edge("Center", "Node2")
    graph.add_edge("Center", "Node3")

    influential_users = graph.most_influential()
    expected_users = [("Center", 1.0)]  # Center is the only most influential user
    if influential_users != expected_users:
        raise check50.Failure("Incorrect most influential user in a star graph.")

@check50.check(test_most_influential_single_path)
def test_equally_influential_users():
    """Multiple equally influential users correctly identified"""
    _, Graph = import_graph()
    graph = Graph()
    graph.add_edge("User1", "User2")
    graph.add_edge("User2", "User3")
    graph.add_edge("User3", "User1")  # Creating a cycle

    influential_users = graph.most_influential()
    expected_users = [("User1", 1.5), ("User2", 1.5), ("User3", 1.5)]  # All users are equally influential
    if influential_users != expected_users:
        raise check50.Failure("Incorrect identification of equally influential users.")


def setup_graph_girvan_newman(Graph):
    graph = Graph()
    edges = [
        ('Marissa', 'Sundar'), ('Marissa', 'Mark'), ('Marissa', 'Elon'),
        ('Sundar', 'Mark'), ('Sundar', 'Elon'), ('Brittany', 'Stephanie'),
        ('Sundar', 'Adam'), ('Sundar', 'Jack'), ('Tim', 'Sundar'),
        ('Jack', 'Adam'), ('Adam', 'Elon'), ('Brittany', 'Serge'),
        ('Elon', 'Mark'), ('Olaf', 'Emanuel'), ('Olaf', 'Rishi'),
        ('Rishi', 'Emanuel'), ('Emanuel', 'Joe'), ('Sundar', "Emanuel"),
        ('Serge', 'Mary')
    ]
    for edge in edges:
        a, b = edge
        graph.add_edge(a, b)
    return graph

@check50.check(shortest_path_direct)
def test_get_communities():
    """Graph partitions into expected communities correctly"""
    _, Graph = import_graph()
    graph = setup_graph_girvan_newman(Graph)
    for c in range(1, 12):
        communities = graph.girvan_newman_algorithm(clusters=c)
        if len(communities) < c:
            raise check50.Failure(f"When asked for {c} clusters, girvan_newman_algorithm(clusters={c}) should return at least {c} clusters.")
        for subgraph in communities:
            if not isinstance(subgraph, (list, set, tuple)):
                raise check50.Failure("Returned subgraphs should be of type list, set, or tuple.")
            if len(subgraph) < 1:
                raise check50.Failure("Ensure girvan_newman_algorithm does not return empty subgraphs.")
    _test_subgraphs(graph, communities)

def _test_subgraphs(graph, result):
    users_all = [i for b in result for i in list(b)]
    for user in graph.keys():
        if users_all.count(user) != 1:
            raise check50.Failure(f"User {user} is not unique across the subgraphs.")


@check50.check(test_get_communities)
def test_compute_sps():
    """Graph computes shortest path correctly"""
    _, Graph = import_graph()
    graph = setup_graph_girvan_newman(Graph)
    if not hasattr(graph, 'sps'):
        raise check50.Failure("Graph should have an attribute named 'sps'.")
    graph.compute_sps()
    node_count = len(graph.keys())
    if len(graph.sps) != node_count:
        raise check50.Failure("SPS matrix dimensions don't match the number of nodes.")
    if [len(i) for i in graph.sps].count(node_count) != node_count:
        raise check50.Failure("SPS matrix dimensions are inconsistent.")
    sp_flag = False
    for i in range(node_count):
        for j in range(node_count):
            if isinstance(graph.sps[i][j], (list, set, tuple)):
                sp_flag = True
                break
        if sp_flag:
            break
    if not sp_flag:
        raise check50.Failure("SPS matrix doesn't seem to contain valid shortest paths.")
