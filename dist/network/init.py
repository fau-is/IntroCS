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
    graph.remove_edge("Alice", "Bob")
    if "Bob" in graph["Alice"]:
        raise check50.Failure("Failed to remove edge between 'Alice' and 'Bob'.")
    if "Alice" in graph["Bob"]:
        raise check50.Failure("Failed to remove edge between 'Bob' and 'Alice'.")
