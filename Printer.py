class Printer:
    @staticmethod
    def print_preorder(node):
        if node is not None:
            print(node.payload, end=", ")
            Printer.print_preorder(node.left)
            Printer.print_preorder(node.right)

    @staticmethod
    def print_inorder(node):
        if node is not None:
            Printer.print_inorder(node.left)
            print(node.payload, end=", ")
            Printer.print_inorder(node.right)

    @staticmethod
    def print_postorder(node):
        if node is not None:
            Printer.print_postorder(node.left)
            Printer.print_postorder(node.right)
            print(node.payload, end=", ")
