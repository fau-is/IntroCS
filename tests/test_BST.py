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

        # Check a few to ensure they're in the correct position
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


    # Task 2
    def test_linear_search(self):
        # Adding some usernames to the BST
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)

        # Test 1: Check if a username can be found
        self.assertEqual(BST.linear_search('Lopinel').username, 'Lopinel')
        self.assertEqual(BST.linear_search('mistur').username, 'mistur')

        # Test 2: Check if a non-existing username returns False
        self.assertFalse(BST.linear_search('NonExistingUser'))

        # Test 3: Check if an empty BST returns False
        BST.root = None
        self.assertFalse(BST.linear_search('Lopinel'))


    def test_binary_search(self):
        # Adding some usernames to the BST
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)

        self.assertEqual(BST.binary_search(BST.root, 'Lopinel').username, 'Lopinel')
        self.assertEqual(BST.binary_search(BST.root, 'mistur').username, 'mistur')

        self.assertFalse(BST.binary_search(BST.root, 'NonExistingUser'))

        BST.root = None
        self.assertFalse(BST.binary_search(BST.root, 'Lopinel'))

    # Task 3
    def test_preorder(self):
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)
        expected_preorder = ["Lopinel", "Harmonia_Amanda", "Dju", "Bram_Finkel", "BrunoBellamy", "GeoffreyDorne", "HyP",
                             "THD_IT", "mistur", "Zestryon"]
        self.assertEqual(BST.preorder(), expected_preorder)

    def test_inorder(self):
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)
        expected_inorder = ["Bram_Finkel", "BrunoBellamy", "Dju", "GeoffreyDorne", "Harmonia_Amanda", "HyP", "Lopinel",
                            "THD_IT", "Zestryon", "mistur"]

        self.assertEqual(BST.inorder(), expected_inorder)

    def test_postorder(self):
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)

        expected_postorder = ["BrunoBellamy", "Bram_Finkel", "GeoffreyDorne", "Dju",  "HyP", "Harmonia_Amanda",
                              "Zestryon", "mistur", "THD_IT", "Lopinel"]
        self.assertEqual(BST.postorder(), expected_postorder)

if __name__ == '__main__':
    unittest.main()
