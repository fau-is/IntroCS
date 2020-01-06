import sys
from Printer import Printer
from bin_search_tree import BST as bst


if __name__ == '__main__':

    INPUT = list(sys.argv[1].split(','))

    # make binary search tree
    bs_tree = bst(INPUT)

    bs_tree.bfs_it()
    bs_tree.dfs_rec()

    # make other bs tree
    bs2_tree = bst(None)
    bs2_tree.add(3)

    # print all variants bst
    # print("Binary Search Tree (1):")
    print("preorder: ", end="")
    Printer.print_preorder(bs_tree.root)
    print("inorder: ", end="")
    Printer.print_inorder(bs_tree.root)
    print("postorder: ", end="")
    Printer.print_postorder(bs_tree.root)
    # print()
    print("find 5:", bs_tree.find(5), end="")

    # print all variants bst
    # print("Binary Search Tree (2):")
    print("preorder: ", end="")
    Printer.print_preorder(bs2_tree.root)
    print("inorder: ", end="")
    Printer.print_inorder(bs2_tree.root)
    print("postorder: ", end="")
    Printer.print_postorder(bs2_tree.root)
    # print()
    print("find 5:", bs2_tree.find(5), end="")
