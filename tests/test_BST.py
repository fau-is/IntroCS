import unittest
from trees.BST import BST
import json

import unittest


class TestBST(unittest.TestCase):

    def setUp(self):
        BST.root = None  # Reset the BST root
        self.bst = BST("Lopinel")  # This will not set as root since add method wasn't called
        self.usernames = ['THD_IT', 'Harmonia_Amanda', 'Dju', 'GeoffreyDorne', 'Bram_Finkel',
                          'HyP', 'mistur', 'Zestryon', 'BrunoBellamy']

    def test_initialization(self):
        self.assertEqual(self.bst.username, "Lopinel")
        self.assertIsNone(self.bst.left)
        self.assertIsNone(self.bst.right)
        self.assertIsNone(BST.root)

    def test_add_root(self):
        BST.add("Lopinel")
        self.assertEqual(BST.root.username, "Lopinel")

    def test_add_nodes(self):
        BST.add("Lopinel")  # Add Lopinel as the root first
        for username in self.usernames:
            BST.add(username)

        # Let's check a few to ensure they're in the correct position
        self.assertEqual(BST.root.username, 'Lopinel')
        self.assertEqual(BST.root.right.username, 'THD_IT')
        self.assertEqual(BST.root.right.right.username, 'mistur')
        self.assertEqual(BST.root.right.left, None)



    def test_tree_structure(self):
        # Ensure that for every node, left child is less than the node and right child is greater
        def is_bst(node):
            if not node:
                return True
            if node.left and node.left.username >= node.username:
                return False
            if node.right and node.right.username <= node.username:
                return False
            return is_bst(node.left) and is_bst(node.right)

        self.assertTrue(is_bst(BST.root))




if __name__ == '__main__':
    unittest.main()
