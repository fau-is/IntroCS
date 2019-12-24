import sys
from Printer import Printer
from avl import avl_tree


if __name__ == '__main__':

    avl1 = avl_tree()
   
    root1 = None
    root1 = avl1.insert(root1, 1)
    root1 = avl1.insert(root1, 2)
    root1 = avl1.insert(root1, 3)
    root1 = avl1.insert(root1, 4)
    root1 = avl1.insert(root1, 5)
    root1 = avl1.insert(root1, 6)
    root1 = avl1.insert(root1, 7)
    root1 = avl1.insert(root1, 8)
    root1 = avl1.insert(root1, 9)
    root1 = avl1.insert(root1, 10)

    Printer.print_inorder(root1)
    Printer.print_preorder(root1)
    Printer.print_postorder(root1)
