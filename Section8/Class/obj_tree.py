class BinTreeNode():
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node: BinTreeNode):
        self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node: BinTreeNode):
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

    @classmethod
    def create_bin_tree(cls, value):
        tree = cls()
        tree.root = BinTreeNode(value)
        return tree

