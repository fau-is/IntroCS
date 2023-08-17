import unittest
from GraphUtils import User, Graph

class TestUser(unittest.TestCase):

    def test_username_initialization(self):
        user = User("Alice")
        self.assertEqual(user.username, "Alice")


class TestGraphMethods(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.user1 = User("Alice")
        self.user2 = User("Bob")
        self.user3 = User("Charlie")
        self.user4 = User("David")
        self.user5 = User("Eve")
        self.user6 = User("Frank")

    def tearDown(self):
        del self.graph

    def test_add_vertex(self):
        self.graph.add_vertex(self.user1)
        self.assertIn("Alice", self.graph)

    def test_add_edge(self):
        self.graph.add_edge(self.user1, self.user2)
        self.assertIn("Bob", self.graph["Alice"])
        self.assertIn("Alice", self.graph["Bob"])

    def test_remove_edge(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.remove_edge((self.user1, self.user2))
        self.assertNotIn("Bob", self.graph["Alice"])
        self.assertNotIn("Alice", self.graph["Bob"])

    def test_dfs(self):
        self._setup_graph_connections()
        visited = self.graph.dfs(self.user1)
        self.assertEqual(visited, ["Alice", "Bob", "Charlie", "David"])
        self._teardown_graph_connections()

    def test_bfs(self):
        self._setup_graph_connections()
        visited = self.graph.bfs(self.user1)
        self.assertEqual(visited, ["Alice", "Bob", "David", "Charlie"])
        self._teardown_graph_connections()

    def test_order_ascending(self):
        self.graph.add_edge(self.user1, self.user4)
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user1, self.user3)
        self.assertEqual(self.graph["Alice"], ["Bob", "Charlie", "David"])

    def _setup_graph_connected(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user2, self.user3)
        self.graph.add_edge(self.user3, self.user4)

    def _setup_graph_disconnected(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user3, self.user4)
        self.graph.add_edge(self.user5, self.user6)

    def test_clusters_connected(self):
        # Test if a fully connected cluster is found
        self._setup_graph_connected()
        clusters = self.graph.find_clusters()
        self.assertEqual(len(clusters), 1)
        self.assertCountEqual(clusters[0], ["Alice", "Bob", "Charlie", "David"])

    def test_clusters_disconnected(self):
        # Test if multiple separated clusters can be found
        self._setup_graph_disconnected()
        clusters = self.graph.find_clusters()
        self.assertEqual(len(clusters), 3)
        for cluster in clusters:
            self.assertIn(len(cluster), [2, 2, 2])

    def _setup_graph_connections(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user2, self.user3)
        self.graph.add_edge(self.user3, self.user4)
        self.graph.add_edge(self.user1, self.user4)

    def _teardown_graph_connections(self):
        self.graph.remove_edge((self.user1, self.user2))
        self.graph.remove_edge((self.user2, self.user3))
        self.graph.remove_edge((self.user3, self.user4))
        self.graph.remove_edge((self.user1, self.user4))


if __name__ == "__main__":
    unittest.main()
