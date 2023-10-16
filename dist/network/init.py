import cs50
import check50.py
from graph import Graph


def import_graph_module():
    try:
        graph_module = check50.py.import_("graph.py")
        return graph_module
    except:
        raise check50.Failure("graph.py not found or has errors.")


@check50.check()
def test_username_initialization():
    """User correctly initialized with username"""
    graph_module = import_graph_module()
    try:
        user = graph_module.User("Alice")
        if not hasattr(user, 'username'):
            raise check50.Failure("User object is missing 'username' attribute.")
        if user.username != "Alice":
            raise check50.Mismatch("Alice", user.username)
    except:
        raise check50.Failure("User initialization failed.")


@check50.check(test_username_initialization)
def test_add_vertex():
    """Vertex added to graph"""
    graph_module = import_graph_module()
    try:
        graph = graph_module.Graph()
        graph.add_vertex(graph_module.User("Alice"))
        if "Alice" not in graph:
            raise check50.Mismatch("Alice", list(graph.keys())[0])
    except:
        raise check50.Failure("Adding vertex failed.")


@check50.check(test_add_vertex)
def test_add_edge():
    """Edge added to graph"""
    graph_module = import_graph_module()
    try:
        graph = graph_module.Graph()
        user1 = graph_module.User("Alice")
        user2 = graph_module.User("Bob")

        graph.add_edge(user1, user2)

        if "Bob" not in graph["Alice"] or "Alice" not in graph["Bob"]:
            raise check50.Failure("Edge between Alice and Bob not established.")
    except:
        raise check50.Failure("Adding edge failed.")


@check50.check(test_add_edge)
def test_remove_edge():
    """Edge removed from graph"""
    graph_module = import_graph_module()
    try:
        graph = graph_module.Graph()
        user1 = graph_module.User("Alice")
        user2 = graph_module.User("Bob")

        graph.add_edge(user1, user2)
        graph.remove_edge(user1, user2)

        if "Bob" in graph["Alice"] or "Alice" in graph["Bob"]:
            raise check50.Failure("Edge between Alice and Bob was not removed.")
    except:
        raise check50.Failure("Removing edge failed.")


@check50.check(test_remove_edge)
def test_order_ascending():
    """Neighbors of vertex are in ascending order"""
    try:
        graph_module = import_graph_module()
        graph = graph_module.Graph()
        user1 = graph_module.User("Alice")
        user2 = graph_module.User("Bob")
        user3 = graph_module.User("Charlie")
        user4 = graph_module.User("David")

        graph.add_edge(user1, user4)
        graph.add_edge(user1, user2)
        graph.add_edge(user1, user3)

        if graph["Alice"] != ["Bob", "Charlie", "David"]:
            raise check50.Mismatch(["Bob", "Charlie", "David"], graph["Alice"])
    except:
        raise check50.Failure("Neighbors are not in ascending order.")


@check50.check(test_order_ascending)
def test_dfs():
    """Depth-first search returns expected order"""
    try:
        graph = graph_module.Graph()
        user1 = graph_module.User("Alice")
        user2 = graph_module.User("Bob")
        user3 = graph_module.User("Charlie")
        user4 = graph_module.User("David")

        graph.add_edge(user1, user2)
        graph.add_edge(user2, user3)
        graph.add_edge(user3, user4)
        graph.add_edge(user1, user4)

        visited = graph.dfs(user1)
        if visited != ["Alice", "Bob", "Charlie", "David"]:
            raise check50.Mismatch(["Alice", "Bob", "Charlie", "David"], visited)
    except:
        raise check50.Failure("Depth-first search failed.")


@check50.check(test_dfs)
def test_clusters_connected():
    """Graph with a fully connected cluster"""
    try:
        graph = graph_module.Graph()
        user1 = graph_module.User("Alice")
        user2 = graph_module.User("Bob")
        user3 = graph_module.User("Charlie")
        user4 = graph_module.User("David")

        graph.add_edge(user1, user2)
        graph.add_edge(user2, user3)
        graph.add_edge(user3, user4)

        clusters = graph.get_subgraphs()
        if len(clusters) != 1:
            raise check50.Failure(f"Expected 1 cluster, got {len(clusters)} clusters.")

        cluster_users = [str(user) for user in clusters[0]]
        if set(cluster_users) != {"Alice", "Bob", "Charlie", "David"}:
            raise check50.Mismatch({"Alice", "Bob", "Charlie", "David"}, set(cluster_users))
    except:
        raise check50.Failure("Failed to correctly identify connected cluster.")


@check50.check(test_clusters_connected)
def test_clusters_disconnected():
    """Multiple separated clusters in graph"""
    try:
        graph = graph_module.Graph()
        user1 = graph_module.User("Alice")
        user2 = graph_module.User("Bob")
        user3 = graph_module.User("Charlie")
        user4 = graph_module.User("David")
        user5 = graph_module.User("Eve")
        user6 = graph_module.User("Frank")

        graph.add_edge(user1, user2)
        graph.add_edge(user3, user4)
        graph.add_edge(user5, user6)

        clusters = graph.get_subgraphs()
        if len(clusters) != 3:
            raise check50.Failure(f"Expected 3 separate clusters, got {len(clusters)} clusters.")

        for cluster in clusters:
            if len(cluster) not in [2, 2, 2]:
                raise check50.Failure("Each disconnected cluster should have 2 users.")
    except:
        raise check50.Failure("Failed to correctly identify disconnected clusters.")


@check50.check(test_clusters_disconnected)
def test_shortest_path_exists():
    """Shortest path exists between nodes"""
    try:
        graph = graph_module.Graph()
        user1 = graph_module.User("Alice")
        user2 = graph_module.User("Bob")
        user3 = graph_module.User("Charlie")
        user4 = graph_module.User("David")
        user5 = graph_module.User("Eve")

        graph.add_edge(user1, user2)
        graph.add_edge(user2, user3)
        graph.add_edge(user3, user4)
        graph.add_edge(user4, user5)
        graph.add_edge(user1, user5)

        path = graph.shortest_path("Alice", "David")
        if path != ["Alice", "Eve", "David"]:
            raise check50.Mismatch(["Alice", "Eve", "David"], path)
    except:
        raise check50.Failure("Failed to find correct shortest path.")


@check50.check(test_shortest_path_exists)
def test_no_shortest_path():
    """No path exists between nodes"""
    try:
        graph = graph_module.Graph()
        user1 = graph_module.User("Alice")
        user2 = graph_module.User("Bob")
        user3 = graph_module.User("Charlie")
        user4 = graph_module.User("David")
        user5 = graph_module.User("Eve")
        user6 = graph_module.User("Frank")

        graph.add_edge(user1, user2)
        graph.add_edge(user2, user3)
        graph.add_edge(user3, user4)
        graph.add_edge(user4, user5)
        graph.add_edge(user1, user5)

        path = graph.shortest_path("Alice", "Frank")
        if path is not None:
            raise check50.Mismatch(None, path)
    except:
        raise check50.Failure("Failed to handle scenario where no path exists.")


@check50.check(test_no_shortest_path)
def test_shortest_path():
    """Validates shortest path between nodes"""
    try:
        graph = graph_module.Graph()
        user1 = graph_module.User("Alice")
        user2 = graph_module.User("Bob")
        user3 = graph_module.User("Charlie")
        user4 = graph_module.User("David")
        user5 = graph_module.User("Eve")

        graph.add_edge(user1, user2)
        graph.add_edge(user2, user3)
        graph.add_edge(user3, user4)
        graph.add_edge(user4, user5)
        graph.add_edge(user1, user5)

        path = graph.shortest_path("Alice", "Eve")
        if path != ["Alice", "Eve"]:
            raise check50.Mismatch(["Alice", "Eve"], path)
    except:
        raise check50.Failure("Failed to find correct shortest path.")


@check50.check(test_shortest_path)
def test_build_graph():
    """Graph building from JSON data"""
    try:
        graph = graph_module.Graph()
        filepath = '../ressources/graph_52n.json'
        with open(filepath, 'r') as f:
            data = json.load(f)

        first_key = list(data.keys())[0]
        del data[first_key]

        graph.parse_data(filepath)

        for key, neighbors in data.items():
            if str(graph_module.User(key)) not in graph:
                raise check50.Failure(f"User {key} is missing in the graph.")
            for neighbor in neighbors:
                if str(graph_module.User(neighbor)) not in graph[str(graph_module.User(key))]:
                    raise check50.Failure(f"Neighbor {neighbor} missing for user {key} in the graph.")
    except:
        raise check50.Failure("Failed to correctly build graph from JSON data.")


def _setup_graph_4_5():
    graph_module = import_graph_module()  # Import the required module
    graph = graph_module.Graph()
    # Define edges for the graph
    Edges = [('Marissa', 'Sundar'), ('Marissa', 'Mark'), ('Marissa', 'Elon'),
             ('Sundar', 'Mark'), ('Sundar', 'Elon'), ('Brittany', 'Stephanie'),
             ('Sundar', 'Adam'), ('Sundar', 'Jack'), ('Tim', 'Sundar'),
             ('Jack', 'Adam'), ('Adam', 'Elon'), ('Brittany', 'Serge'),
             ('Elon', 'Mark'), ('Olaf', 'Emanuel'), ('Olaf', 'Rishi'),
             ('Rishi', 'Emanuel'), ('Emanuel', 'Joe'), ('Sundar', "Emanuel"),
             ('Serge', 'Mary')]

    for edge in Edges:
        a, b = edge
        graph.add_edge(a, b)  # Add edges to the graph

    return graph


@check50.check(test_shortest_path)
def test_build_graph():
    """Graph building from JSON data"""
    try:
        graph = graph_module.Graph()
        filepath = '../ressources/graph_52n.json'
        with open(filepath, 'r') as f:
            data = json.load(f)

        first_key = list(data.keys())[0]
        del data[first_key]

        graph.parse_data(filepath)

        for key, neighbors in data.items():
            if str(graph_module.User(key)) not in graph:
                raise check50.Failure(f"User {key} is missing in the graph.")
            for neighbor in neighbors:
                if str(graph_module.User(neighbor)) not in graph[str(graph_module.User(key))]:
                    raise check50.Failure(f"Neighbor {neighbor} missing for user {key} in the graph.")
    except:
        raise check50.Failure("Failed to correctly build graph from JSON data.")


@check50.check(test_build_graph)
def test_most_influential():
    """Identifies most influential user"""
    try:
        graph = graph_module.Graph()
        # Assuming this setup method sets up a specific scenario for most influential user.
        # You can replace this with the actual setup for the scenario if needed.
        _setup_graph_4_5()

        result = graph.most_influential()
        if not isinstance(result, tuple) or len(result) != 2:
            raise check50.Failure("Expected result to be a tuple of length 2.")

        if result[0] != "Sundar":
            raise check50.Mismatch("Sundar", result[0])

        if not (2.3 <= result[1] <= 2.4):
            raise check50.Mismatch("Influence score between 2.3 and 2.4", result[1])
    except:
        raise check50.Failure("Failed to identify the most influential user correctly.")


@check50.check(test_most_influential)
def test_get_communities():
    """Identifies subgraphs or communities in graph"""
    try:
        graph = graph_module.Graph()
        _setup_graph_4_5()

        communities = graph.girvan_newman_algorithm(clusters=11)
        if not all([isinstance(subgraph, (list, set, tuple)) for subgraph in communities]):
            raise check50.Failure("Returned subgraphs should be of type list, set, or tuple.")

        users_all = [i for community in communities for i in list(community)]
        for user in graph.keys():
            if users_all.count(user) != 1:
                raise check50.Failure(f"User {user} is not unique across the subgraphs.")
    except:
        raise check50.Failure("Failed to correctly identify subgraphs or communities.")


@check50.check(test_get_communities)
def test_compute_sps():
    """Validates computation of shortest path scores"""
    try:
        graph = graph_module.Graph()
        _setup_graph_4_5()

        if not hasattr(graph, 'sps'):
            raise check50.Failure("Graph should have an attribute named 'sps'.")

        graph.compute_sps()
        node_count = len(graph.keys())

        if len(graph.sps) != node_count:
            raise check50.Failure(f"Expected SPS matrix with {node_count} rows, got {len(graph.sps)} rows.")

        if not all([len(row) == node_count for row in graph.sps]):
            raise check50.Failure("SPS matrix dimensions are inconsistent.")

        if not any([isinstance(cell, (list, set, tuple)) for row in graph.sps for cell in row]):
            raise check50.Failure("SPS matrix doesn't seem to contain valid shortest paths.")
    except:
        raise check50.Failure("Failed to compute shortest path scores correctly.")
