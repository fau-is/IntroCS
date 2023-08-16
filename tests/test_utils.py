import unittest
import sys
import os
from GraphUtils import *


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

    def test_add_vertex(self):
        self.graph.add_vertex(self.user1)
        self.assertIn("Alice", self.graph)

    def test_add_edge(self):
        self.graph.add_edge(self.user1, self.user2)
        self.assertIn("Bob", self.graph["Alice"])
        self.assertIn("Alice", self.graph["Bob"])
        self.graph.remove_edge((self.user1, self.user2))

    def test_remove_edge(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.remove_edge((self.user1, self.user2))
        self.assertNotIn("Bob", self.graph["Alice"])
        self.assertNotIn("Alice", self.graph["Bob"])

    def test_dfs(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user2, self.user3)
        self.graph.add_edge(self.user3, self.user4)
        self.graph.add_edge(self.user1, self.user4)
        visited = self.graph.dfs(self.user1)
        self.assertEqual(visited, ["Alice", "Bob", "Charlie", "David"])
        self.graph.remove_edge((self.user1, self.user2))
        self.graph.remove_edge((self.user2, self.user3))
        self.graph.remove_edge((self.user3, self.user4))
        self.graph.remove_edge((self.user1, self.user4))

    def test_bfs(self):
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user2, self.user3)
        self.graph.add_edge(self.user3, self.user4)
        self.graph.add_edge(self.user1, self.user4)
        visited = self.graph.bfs(self.user1)
        self.assertEqual(visited, ["Alice", "Bob", "David", "Charlie"])
        self.graph.remove_edge((self.user1, self.user2))
        self.graph.remove_edge((self.user2, self.user3))
        self.graph.remove_edge((self.user3, self.user4))
        self.graph.remove_edge((self.user1, self.user4))

    def test_order_ascending(self):
        self.graph.add_edge(self.user1, self.user4)
        self.graph.add_edge(self.user1, self.user2)
        self.graph.add_edge(self.user1, self.user3)
        self.assertEqual(self.graph["Alice"], ["Bob", "Charlie", "David"])
        self.graph.remove_edge((self.user1, self.user4))
        self.graph.remove_edge((self.user1, self.user2))
        self.graph.remove_edge((self.user1, self.user3))



if __name__ == "__main__":
    unittest.main()