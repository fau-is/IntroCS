import unittest
from tree import BinTree, BinTreeNode

def tree_builder1():
    root = BinTreeNode("Root")
    root.left = BinTreeNode("RootLeft")
    root.left.left = BinTreeNode("RootLeftLeft")
    root.left.right = BinTreeNode("RootLeftRight")

class TestTreeBuilder(unittest.TestCase):
    def setUp(self):
        self.tree = tree_builder1()

    def test_create_root(self):
        tree = BinTree("Root")

        self.assertEqual("Root", tree.root.value)

    def test_add_nodes_to_empty_tree(self):
        self.tree = BinTree("Root")

        self.tree.add_node("RootLeft")
        self.tree.add_node("RootRight")

        self.assertEqual("RootLeft", self.tree.root.left.value)
        self.assertEqual("RootRight", self.tree.root.right.value)




if __name__ == "__main__":
    unittest.main()

