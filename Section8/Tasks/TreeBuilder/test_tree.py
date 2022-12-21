import unittest
from tree import BinTree, BinTreeNode

def tree_builder1():
    root = BinTreeNode("Root")
    root.left = BinTreeNode("RootLeft")
    root.left.left = BinTreeNode("RootLeftLeft")
    root.left.right = BinTreeNode("RootLeftRight")

    return root

class TestTreeBuilder(unittest.TestCase):
    def setUp(self):
        self.root = tree_builder1()

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
        self.tree.add_node("RootRight")
        self.assertEqual("RootRight", self.root.right.value)




if __name__ == "__main__":
    unittest.main()

