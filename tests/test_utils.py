import unittest
from GraphUtils import User, Graph
import json

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

    # Task 1
    def _setup_graph_dfs_bfs(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user2, self.user3)
        self.graph.add_edge(self.user3, self.user4)
        self.graph.add_edge(self.user1, self.user4)

    def _teardown_graph_connections(self):
        self.graph.remove_edge((self.user1, self.user2))
        self.graph.remove_edge((self.user2, self.user3))
        self.graph.remove_edge((self.user3, self.user4))
        self.graph.remove_edge((self.user1, self.user4))

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
        self._setup_graph_dfs_bfs()
        visited = self.graph.dfs(self.user1)
        self.assertEqual(visited, ["Alice", "Bob", "Charlie", "David"])
        self._teardown_graph_connections()

    def test_bfs(self):
        self._setup_graph_dfs_bfs()
        visited = self.graph.bfs(self.user1)
        self.assertEqual(visited, ["Alice", "Bob", "David", "Charlie"])
        self._teardown_graph_connections()

    def test_order_ascending(self):
        self.graph.add_edge(self.user1, self.user4)
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user1, self.user3)
        self.assertEqual(self.graph["Alice"], ["Bob", "Charlie", "David"])



    # task 2
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


    # Task 3
    def _setup_graph(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user2, self.user3)
        self.graph.add_edge(self.user3, self.user4)
        self.graph.add_edge(self.user4, self.user5)
        self.graph.add_edge(self.user1, self.user5)

    def test_bfs_find_path_exists(self):
        self._setup_graph()
        path = self.graph.bfs_find("Alice", "David")
        self.assertEqual(path, ["Alice", "Eve", "David"])

    def test_bfs_find_no_path(self):
        self._setup_graph()
        path = self.graph.bfs_find("Alice", "Frank")
        self.assertEqual(path, None)

    def test_bfs_find_shortest_path(self):
        self._setup_graph()
        path = self.graph.bfs_find("Alice", "Eve")
        self.assertEqual(path, ["Alice", "Eve"])

    # Task 4
    def setUp_JSON_data(self):
        self.graph = Graph()
        self.filepath = 'ressources/graph_52n.json'
        with open(self.filepath, 'r') as f:
            self.data = json.load(f)
        # Remove the first key-item pair as per the build_graph method
        first_key = list(self.data.keys())[0]
        del self.data[first_key]


    def test_build_graph(self):
        self.setUp_JSON_data()
        self.graph.build_graph(self.filepath)

        # Check if graph has been built correctly
        for key, neighbors in self.data.items():
            self.assertTrue(str(User(key)) in self.graph)
            for neighbor in neighbors:
                self.assertIn(str(User(neighbor)), self.graph[str(User(key))])

    def test_most_influential(self):
        self.setUp_JSON_data()
        self.graph.build_graph(self.filepath)
        result = self.graph.most_influential()
        # Check if result is a tuple of length 2
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(len(result), 2)

        # Check if the first element of the tuple is a string or instance of User with the value "paulfree14"
        self.assertTrue(isinstance(result[0], (str, User)))
        self.assertEqual(result[0], "paulfree14")

        # Check if the second element of the tuple is a float with a value between 2.4 and 2.5
        self.assertTrue(isinstance(result[1], float))
        self.assertTrue(2.4 <= result[1] <= 2.5)




if __name__ == "__main__":
    unittest.main()
