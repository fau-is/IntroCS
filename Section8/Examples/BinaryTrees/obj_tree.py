from graphviz import Graph

class BinTreeNode():
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node):
        self.__right = node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self):
        self.__value = value




class BinTree():
    def __init__(self):
        self.root = None

    def tree_drawer(self):
        g = Graph()
        g.attr('node', fillcolor='white', fontcolor='black', shape='circle', style='filled', border='black')
        BinTree.__rec_helper(self.root, g)
        g.render(filename="bto", format="png")

    @classmethod
    def create_bin_tree(cls, value):
        tree = cls()
        tree.root = BinTreeNode(value)
        return tree

    @staticmethod
    def __rec_helper(node, g):
        if node == None:
            return

        g.node(str(node.value), str(node.value))
        if node.left:
            BinTree.__rec_helper(node.left, g)
            g.edge(str(node.value), str(node.left.value))
        if node.right:
            BinTree.__rec_helper(node.right, g)
            g.edge(str(node.value), str(node.right.value))


if __name__ == "__main__":
    btree = BinTree.create_bin_tree(1)
    btree.root.left = BinTreeNode(2)
    btree.root.right = BinTreeNode(3)
    btree.root.right.left = BinTreeNode(4)
    btree.root.right.right = BinTreeNode(5)

    btree.tree_drawer()





