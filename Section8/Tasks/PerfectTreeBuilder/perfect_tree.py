from graphviz import Graph

class BinTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_height(self):
        if not self.left and not self.right:
            return 0
        if self.left and self.right:
            return min(self.right.get_height(), self.left.get_height()) + 1
        if self.right and not self.left:
            return self.right.get_height() + 1
        else:
            return self.left.get_height() + 1

    def add_node(self, value):
        if not self.left:
            self.left = BinTreeNode(value)
        elif not self.right:
            self.right = BinTreeNode(value)
        elif self.left.get_height() < self.right.get_height():
            self.left.add_node(value)
        else:
            self.right.add_node(value)

    def print_preorder(self):
        print(self.value)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def draw_tree(self, graph):
        graph.node(str(self.value), str(self.value))

        if self.left:
            self.left.draw_tree(graph)
            graph.edge(str(self.value), str(self.left.value))

        if self.right:
            self.right.draw_tree(graph)
            graph.edge(str(self.value), str(self.right.value))



class BinTree:
    def __init__(self, value):
        self.root = BinTreeNode(value)

    def add_node(self, value):
        self.root.add_node(value)

    def print_tree(self):
        self.root.print_preorder()

    def draw_tree(self, name="ptree"):
        g = Graph()
        g.attr('node', fillcolor='white', fontcolor='black', shape='circle', style='filled', border='black')
        self.root.draw_tree(g)

        g.render(filename=name, format="png")

if __name__ == "__main__":
    tree = BinTree(1)
    tree.add_node(2)
    tree.add_node(3)
    tree.add_node(4)
    tree.add_node(5)

    tree.print_tree()
    tree.draw_tree()