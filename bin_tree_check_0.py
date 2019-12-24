import sys
from Printer import Printer
from avl import avl_tree


if __name__ == '__main__':

    avl0 = avl_tree()
    avl1 = avl_tree()
    
    root0 = None
    root0 = avl0.insert(root0, 10)
    root0 = avl0.insert(root0, 20)
    root0 = avl0.insert(root0, 30)
    root0 = avl0.insert(root0, 40)
    root0 = avl0.insert(root0, 50)
    root0 = avl0.insert(root0, 25)

    Printer.print_inorder(root0)
    Printer.print_preorder(root0)
    Printer.print_postorder(root0)
