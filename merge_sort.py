from Node import Node


class BinTree:

    @staticmethod
    def make_bt(arg_tree):
        return BinTree.make_bt_helper(arg_tree, None, 0, len(arg_tree))

    @staticmethod
    def make_bt_helper(arr, node, parent, n):
        if parent < n:
            temp = Node(arr[parent])
            node = temp

            node.left = BinTree.make_bt_helper(arr, node.left, 2 * parent + 1, n)
            node.right = BinTree.make_bt_helper(arr, node.right, 2 * parent + 2, n)

        return node

