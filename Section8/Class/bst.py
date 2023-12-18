from graphviz import Graph


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def find(self, value):
        if self.value == value:
            return True
        elif value > self.value and self.right is not None:
            return self.right.find(value)
        elif value < self.value and self.left is not None:
            return self.left.find(value)
        else:
            return False

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

    def remove_node(self, value):
        current = self
        found = None
        parent = None
        while not found:
            if current.value == value:
                found = current
            else:
                parent = current
                if value < self.value and current.left is not None:
                    current = current.left
                elif value > self.value and current.right is not None:
                    current = current.right
                else:
                    return
        if found.left and found.right:
            self.__remove_two(found, parent)
        elif found.left or found.right:
            self.__remove_one(found, parent)
        else:
            if found == parent.left:
                parent.left = None
            else:
                parent.right = None

    def __remove_two(self, found, parent):
        pass




    def __remove_one(self, found, parent):
        if parent.left == found:
            if found.right:
                parent.left = found.right
            else:
                parent.left = found.left
        else:
            if found.right:
                parent.right = found.right
            else:
                parent.right = found.left


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
    root.remove_node(1)
    root.remove_node(7)
    draw_bst(root)








