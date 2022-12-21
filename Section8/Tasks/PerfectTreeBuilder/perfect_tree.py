class BinTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_height(self)
        if not self.left and not self.right:
            return 0
        if self.left and self.right:
            return max(self.right.get_height(), self.left.get_height()) + 1
        if self.right and not self.left:
            return self.right.get_height() + 1
        else:
            return self.left.get_height() + 1

    def add_node(self, value)
        if self.left is None:
            self.left