class BinTreeNode():
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

class BinTree():
    def __init__(self):
        self.root = None

    @classmethod
    def create_bin_tree(cls, value):
        tree = cls()
        tree.root = BinTreeNode(value)
        return tree

    def 