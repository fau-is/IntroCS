import unittest
from binary_search_tree import BST



class TestBST(unittest.TestCase):

    def setUp(self):
        BST.root = None  # Reset the BST root
        self.bst = BST("Lopinel")  # This will not set as root since add method wasn't called
        self.usernames = ['THD_IT', 'Harmonia_Amanda', 'Dju', 'GeoffreyDorne', 'Bram_Finkel',
                          'HyP', 'mistur', 'Zestryon', 'BrunoBellamy']

    def test_initialization(self):
        # Tests that a BST node is correctly initialized with the provided username and that its left and right
        # children are None.
        self.assertEqual(self.bst.username, "Lopinel", "Failed to initialize the BST object with the correct username.")
        self.assertIsNone(self.bst.left, "Left child should be None upon initialization.")
        self.assertIsNone(self.bst.right, "Right child should be None upon initialization.")
        self.assertIsNone(BST.root, "Root should be None since the add method wasn't called during setup.")

    def test_add_root(self):
        # Tests that a root node can be added to the BST.
        BST.add("Lopinel")
        self.assertEqual(BST.root.username, "Lopinel", "Failed to add the root node.")

    def test_add_nodes(self):
        # Tests the addition of multiple nodes to ensure they are placed correctly in the BST.
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)
        self.assertEqual(BST.root.username, 'Lopinel', "Root node is incorrect.")
        self.assertEqual(BST.root.right.username, 'THD_IT', "Right child of the root is not correct.")
        self.assertEqual(BST.root.right.right.username, 'mistur', "Right child of the THD_IT node is not correct.")
        self.assertIsNone(BST.root.right.left, "Left child of the THD_IT node should be None.")

    def test_tree_structure(self):
        # Tests that the entire Mastodon_tree adheres to the BST properties: left child < parent and right child > parent.
        def is_bst(node):
            if not node:
                return True
            if node.left and node.left.username >= node.username:
                return False
            if node.right and node.right.username <= node.username:
                return False
            return is_bst(node.left) and is_bst(node.right)
        self.assertTrue(is_bst(BST.root), "The BST structure is incorrect. Ensure left child < parent and right child > parent.")

    def test_linear_search(self):
        # Tests the linear search method to find existing users in the BST and ensure non-existing users and an empty BST return False.
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)
        self.assertEqual(BST.linear_search('Lopinel').username, 'Lopinel', "Linear search failed to find 'Lopinel'.")
        self.assertEqual(BST.linear_search('mistur').username, 'mistur', "Linear search failed to find 'mistur'.")
        self.assertFalse(BST.linear_search('NonExistingUser'), "Linear search should return False for non-existing users.")
        BST.root = None
        self.assertFalse(BST.linear_search('Lopinel'), "Linear search should return False for an empty BST.")

    def test_binary_search(self):
        # Tests the binary search method to find existing users in the BST and ensure non-existing users and an empty BST return False.
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)
        self.assertEqual(BST.binary_search(BST.root, 'Lopinel').username, 'Lopinel', "Binary search failed to find 'Lopinel'.")
        self.assertEqual(BST.binary_search(BST.root, 'mistur').username, 'mistur', "Binary search failed to find 'mistur'.")
        self.assertFalse(BST.binary_search(BST.root, 'NonExistingUser'), "Binary search should return False for non-existing users.")
        BST.root = None
        self.assertFalse(BST.binary_search(BST.root, 'Lopinel'), "Binary search should return False for an empty BST.")

    def test_preorder(self):
        # Tests that the preorder traversal of the BST returns the expected order of usernames.
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)
        expected_preorder = ["Lopinel", "Harmonia_Amanda", "Dju", "Bram_Finkel", "BrunoBellamy", "GeoffreyDorne", "HyP",
                             "THD_IT", "mistur", "Zestryon"]
        self.assertEqual(BST.preorder(), expected_preorder, "Preorder traversal does not match the expected order.")

    def test_inorder(self):
        # Tests that the inorder traversal of the BST returns the expected order of usernames.
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)
        expected_inorder = ["Bram_Finkel", "BrunoBellamy", "Dju", "GeoffreyDorne", "Harmonia_Amanda", "HyP", "Lopinel",
                            "THD_IT", "Zestryon", "mistur"]
        self.assertEqual(BST.inorder(), expected_inorder, "Inorder traversal does not match the expected order.")

    def test_postorder(self):
        # Tests that the postorder traversal of the BST returns the expected order of usernames.
        BST.add("Lopinel")
        for username in self.usernames:
            BST.add(username)
        expected_postorder = ["BrunoBellamy", "Bram_Finkel", "GeoffreyDorne", "Dju",  "HyP", "Harmonia_Amanda",
                              "Zestryon", "mistur", "THD_IT", "Lopinel"]
        self.assertEqual(BST.postorder(), expected_postorder, "Postorder traversal does not match the expected order.")

if __name__ == '__main__':
    unittest.main()