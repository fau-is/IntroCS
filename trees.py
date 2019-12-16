import sys
from Printer import Printer
from bin_tree import BinTree as bt
from bin_search_tree import BinSearchTree as bst


if __name__ == '__main__':

    INPUT = list(sys.argv[1].split(','))

    # make binary tree
    bin_tree = bt.make_bt(INPUT)

    # make binary search tree
    bs_tree = bst(INPUT)

    bs_tree.bfs_it()
    bs_tree.dfs_rec()

    # print all variants bt
    print("Binary Tree:")
    print("\t preorder: \t", end="")
    Printer.print_preorder(bin_tree)
    print("\n\t inorder: \t", end="")
    Printer.print_inorder(bin_tree)
    print("\n\t postorder: \t", end="")
    Printer.print_postorder(bin_tree)
    print()

    # print all variants bst
    print("Binary Search Tree:")
    print("\t preorder: \t", end="")
    Printer.print_preorder(bs_tree.root)
    print("\n\t inorder: \t", end="")
    Printer.print_inorder(bs_tree.root)
    print("\n\t postorder: \t", end="")
    Printer.print_postorder(bs_tree.root)
