from graphviz import Graph


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def find(self, value):
        if self.value == value:
            return self
        elif value > self.value and self.right is not None:
            return self.right.find(value)
        elif value < self.value and self.left is not None:
            return self.left.find(value)

    def add_node(self, value):
        if self.value == value:
            return
        elif value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.add_node(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.add_node(value)

    def find_max(self):
        if self.right is not None:
            return self.right.find_max()
        else:
            return self.value

    def rem_node(self,value):
        if value < self.value:
            if self.left is not None:
                self.left = self.left.rem_node(value)
            return self
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.rem_node(value)
            return self
        else:
            if self.right is None and self.left is None:
                return None
            elif self.right is not None and self.left is None:
                return self.right
            elif self.right is None and self.left is not None:
                return self.left
            else:
                self.value = self.left.find_max()
                self.left = self.left.rem_node(self.value)
                return self


def draw_bst(root):
    g = Graph()
    g.attr('node', fillcolor='white', fontcolor='black', shape='circle', style='filled', border='black')
    g.node(str(root.value), str(root.value))

    stack = [root]

    while stack:
        node = stack.pop()
        if node.left is not None:
            g.node(str(node.left.value), str(node.left.value))
            g.edge(str(node.value), str(node.left.value))
            stack.append(node.left)
        if node.right is not None:
            g.node(str(node.right.value), str(node.right.value))
            g.edge(str(node.value), str(node.right.value))
            stack.append(node.right)

    g.render(filename="bst", format="png")


if __name__ == '__main__':
    root = BST(5)
    root.add_node(3)
    root.add_node(4)
    root.add_node(2)
    root.add_node(1)
    root.add_node(8)
    root.add_node(7)
    root.add_node(9)
    root.add_node(6)
    root.rem_node(3)
    root.rem_node(8)
    draw_bst(root)








