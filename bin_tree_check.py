import sys
from bin_tree import BinTree as bt
from Printer import Printer


if __name__ == '__main__':

    INPUT = list(sys.argv[1].split(','))

    # make binary tree
    bin_tree = bt.make_bt(INPUT)

    # print all variants bt
    print("preorder: ", end="")
    Printer.print_preorder(bin_tree)
    print("inorder: ", end="")
    Printer.print_inorder(bin_tree)
    print("postorder: ", end="")
    Printer.print_postorder(bin_tree)
