import unittest
from graph import User, Graph
import json

class TestUser(unittest.TestCase):

    def test_username_initialization(self):
        user = User("Alice")
        self.assertTrue(hasattr(user, 'username'))
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
        self.assertIn("Alice", self.graph, "Failed to add vertex 'Alice' to the graph.")

    def test_add_edge(self):
        self.graph.add_edge(self.user1, self.user2)
        self.assertIn("Bob", self.graph["Alice"], "Failed to establish an edge between 'Alice' and 'Bob'.")
        self.assertIn("Alice", self.graph["Bob"], "Failed to establish an edge between 'Bob' and 'Alice'.")

    def test_remove_edge(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.remove_edge((self.user1, self.user2))
        self.assertNotIn("Bob", self.graph["Alice"], "Failed to remove edge between 'Alice' and 'Bob'.")
        self.assertNotIn("Alice", self.graph["Bob"], "Failed to remove edge between 'Bob' and 'Alice'.")


    def test_order_ascending(self):
        self.graph.add_edge(self.user1, self.user4)
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user1, self.user3)
        self.assertEqual(self.graph["Alice"], ["Bob", "Charlie", "David"], "Neighbors of vertex are not in ascending order.")

    def test_dfs(self):
        self._setup_graph_dfs_bfs()
        visited = self.graph.dfs(self.user1)
        self.assertEqual(visited, ["Alice", "Bob", "Charlie", "David"], "Depth-first search did not return the expected order.")
        self._teardown_graph_connections()

    # def test_bfs(self):
    #     """
    #     no need for this test at the moment
    #     :return:
    #     """
    #     self._setup_graph_dfs_bfs()
    #     visited = self.graph.bfs(self.user1)
    #     self.assertEqual(visited, ["Alice", "Bob", "David", "Charlie"])
    #     self._teardown_graph_connections()



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
        clusters = self.graph.get_subgraphs()
        self.assertEqual(len(clusters), 1, "Expected 1 cluster for a fully connected graph.")
        self.assertCountEqual(clusters[0], ["Alice", "Bob", "Charlie", "David"], "Connected cluster doesn't match the expected users.")
        self._test_subgraphs(clusters)

    def test_clusters_disconnected(self):
        # Test if multiple separated clusters can be found
        self._setup_graph_disconnected()
        clusters = self.graph.get_subgraphs()
        self.assertEqual(len(clusters), 3, "Expected 3 separate clusters for the given graph.")
        for cluster in clusters:
            self.assertIn(len(cluster), [2, 2, 2], "Each disconnected cluster should have 2 users.")
        self._test_subgraphs(clusters)


    # Task 3
    def _setup_graph(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user2, self.user3)
        self.graph.add_edge(self.user3, self.user4)
        self.graph.add_edge(self.user4, self.user5)
        self.graph.add_edge(self.user1, self.user5)

    def test_shortest_path_exists(self):
        self._setup_graph()
        path = self.graph.shortest_path("Alice", "David")
        self.assertEqual(path, ["Alice", "Eve", "David"], "Shortest path from 'Alice' to 'David' is incorrect.")

    def test_no_shortest_path(self):
        self._setup_graph()
        path = self.graph.shortest_path("Alice", "Frank")
        self.assertEqual(path, None, "Expected no path between 'Alice' and 'Frank', but a path was returned.")

    def test_shortest_path(self):
        self._setup_graph()
        path = self.graph.shortest_path("Alice", "Eve")
        self.assertEqual(path, ["Alice", "Eve"], "Shortest path between 'Alice' and 'Eve' is incorrect.")

    # Task 4
    def setUp_JSON_data(self):
        self.graph = Graph()
        self.filepath = '../ressources/graph_52n.json'
        with open(self.filepath, 'r') as f:
            self.data = json.load(f)
        # Remove the first key-item pair as per the build_graph method
        first_key = list(self.data.keys())[0]
        del self.data[first_key]


    def test_build_graph(self):
        self.setUp_JSON_data()
        self.graph.parse_data(self.filepath)
        # Check if graph has been built correctly
        for key, neighbors in self.data.items():
            self.assertTrue(str(User(key)) in self.graph, f"User {key} is missing in the graph.")
            for neighbor in neighbors:
                self.assertIn(str(User(neighbor)), self.graph[str(User(key))], f"Neighbor {neighbor} missing for user {key} in the graph.")

    def test_most_influential(self):
        self._setup_graph_4_5()
        result = self.graph.most_influential()
        # Check if result is a tuple of length 2
        self.assertTrue(isinstance(result, tuple), "Expected result to be a tuple.")
        self.assertEqual(len(result), 2, "Expected tuple of length 2 for most influential result.")

        # Check first element of the tuple
        self.assertTrue(isinstance(result[0], (str, User)), "First element of the result should be a string or User instance.")
        self.assertEqual(result[0], "Sundar", "Expected 'Sundar' as the most influential user.")

        # Check second element of the tuple
        self.assertTrue(isinstance(result[1], float), "Second element of the result should be a float.")
        self.assertTrue(2.3 <= result[1] <= 2.4, "Expected influence score between 2.3 and 2.4.")


    # task 5
    def _setup_graph_4_5(self):
        self.graph = Graph()
        Edges = [('Marissa', 'Sundar'), ('Marissa', 'Mark'), ('Marissa', 'Elon'),
                 ('Sundar', 'Mark'), ('Sundar', 'Elon'), ('Brittany', 'Stephanie'),
                 ('Sundar', 'Adam'), ('Sundar', 'Jack'), ('Tim', 'Sundar'),
                 ('Jack', 'Adam'), ('Adam', 'Elon'), ('Brittany', 'Serge'),
                 ('Elon', 'Mark'), ('Olaf', 'Emanuel'), ('Olaf', 'Rishi'),
                 ('Rishi', 'Emanuel'), ('Emanuel', 'Joe'), ('Sundar', "Emanuel"),
                 ('Serge', 'Mary')]

        for edge in Edges:
            a, b = edge
            self.graph.add_edge(a, b)

    def test_get_communities(self):
        self._setup_graph_4_5()
        for c in range(1,12):
            communities = self.graph.girvan_newman_algorithm(clusters=c)
            self.assertGreaterEqual(len(communities), c, f"When asked for {c} clusters, get_communities(clusters={c}) should return at least {c} clusters.")
            for subgraph in communities:
                self.assertTrue(isinstance(subgraph, (list, set, tuple)), "Returned subgraphs should be of type list, set, or tuple.")
                self.assertGreaterEqual(len(subgraph), 1, "Ensure get_communities does not return empty subgraphs.")
        self._test_subgraphs(communities)

    def _test_subgraphs(self, result):
        # every graph node (user) needs to be part of exactly one subgraph
        users_all = [i for b in result for i in list(b)]
        for user in self.graph.keys():
            self.assertEqual(users_all.count(user), 1, f"User {user} is not unique across the subgraphs.")


    def test_compute_sps(self):
        self.assertTrue(hasattr(self.graph, 'sps'), "Graph should have an attribute named 'sps'.")

        self._setup_graph_4_5()
        self.graph.compute_sps()

        node_count = len(self.graph.keys())
        self.assertEqual(len(self.graph.sps), node_count, "SPS matrix dimensions don't match the number of nodes.")
        self.assertEqual([len(i) for i in self.graph.sps].count(node_count), node_count, "SPS matrix dimensions are inconsistent.")

        sp_flag = False
        for i in range(node_count):
            for j in range(node_count):
                if isinstance(self.graph.sps[i][j],(list, set, tuple)):
                    sp_flag = True
                    break
            if sp_flag:
                break
        self.assertTrue(sp_flag, "SPS matrix doesn't seem to contain valid shortest paths.")







if __name__ == "__main__":
    unittest.main()
