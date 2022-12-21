import unittest
from tree import BinTree, BinTreeNode

def tree_builder_root_right_missing():
    root = BinTreeNode("Root")
    root.left = BinTreeNode("RootLeft")
    root.left.left = BinTreeNode("RootLeftLeft")
    root.left.right = BinTreeNode("RootLeftRight")

    return root

def tree_builder_root_left_right_left_missing():
    root = BinTreeNode("Root")
    root.left = BinTreeNode("RootLeft")
    root.left.left = BinTreeNode("RootLeftLeft")
    root.left.left.left = BinTreeNode("RootLeftLeftLeft")
    root.left.left.right = BinTreeNode("RootLeftLeftRight")
    root.left.right.right = BinTreeNode("RootLeftRightRight")
    root.right = BinTreeNode("RootRight")
    root.right.right = BinTreeNode("RootRightRight")
    root.right.right.left = BinTreeNode("RootRightRightLeft")
    root.right.right.right = BinTreeNode("RootRightRightRight")
    root.right.left = BinTreeNode("RootRightLeft")
    root.right.left.left = BinTreeNode("RootRightLeftLeft")
    root.right.left.right = BinTreeNode("RootRightLeftRight")
    return root

class TestTreeBuilder(unittest.TestCase):
    def setUp(self):
        self.root_right_missing = tree_builder_root_right_missing()
        self.root_left_right_left_missing = tree_builder_root_left_right_left_missing()

    def test_create_root(self):
        tree = BinTree("Root")

        self.assertEqual("Root", tree.root.value)

    def test_add_nodes_to_empty_tree(self):
        tree = BinTree("Root")

        tree.add_node("RootLeft")
        tree.add_node("RootRight")

        self.assertEqual("RootLeft", tree.root.left.value)
        self.assertEqual("RootRight", tree.root.right.value)

    def test_add_node_to_filled_tree(self):
        self.root_right_missing.add_node("RootRight")
        self.assertEqual("RootRight", self.root_right_missing.right.value)

    def test_add_node_to_filled_tree(self):
        self.root_left_right_left_missing.add_node("RootLeftRightLeft")
        self.assertEqual("RootLeftRightLeft", self.root_left_right_left_missing.left.right.left.value)




if __name__ == "__main__":
    unittest.main()

