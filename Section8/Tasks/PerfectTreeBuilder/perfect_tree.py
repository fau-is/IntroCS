class BinTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_height(self)
        if not self.left and not self.right:
            return 0
        if self.left and self.right:
            return min(self.right.get_height(), self.left.get_height()) + 1
        if self.right and not self.left:
            return self.right.get_height() + 1
        else:
            return self.left.get_height() + 1

    def add_node(self, value)
        if self.left is None:
            self.left = BinTreeNode(value)
        elif self.right is None:
            self.left = BinTreeNode(value)
        elif self.left.get_height() < self.right.get_height():
            self.left.add_node(value)
        else:
            self.right.add_node

    def print_preorder(self):
        print(self.value)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

class BinTree:
    def __init__(self, value):
        self.root = BinTreeNode(value)

    def add_node(self, value):
        self.root 