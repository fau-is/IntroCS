from Node import Node


class BinSearchTree:

    def __init__(self, arr):
        if arr is None:
            self.root = None
        else:
            self.root = None
            self.root = self.make_bst(arr)

    @staticmethod
    def add(root, value):
        if root.payload < value:
            if root.right is None:
                root.right = Node(value)
            else:
                BinSearchTree.add(root.right, value)
        else:
            if root.left is None:
                root.left = Node(value)
            else:
                BinSearchTree.add(root.left, value)

    def delete(self, value):
        BinSearchTree.delete_helper(self.root, value)

    @staticmethod
    def delete_helper(root, value):
        if root is None:
            return root
        if value < root.payload:
            root.left = BinSearchTree.delete_helper(root.left, value)
        elif value > root.payload:
            root.right = BinSearchTree.delete_helper(root.right, value)
        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            current = root.right
            while current.left is not None:
                current = current.left

            root.payload = current.payload

            root.right = BinSearchTree.delete_helper(root.right, root.payload)

        return root

    @staticmethod
    def min_finder(node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def bfs_it(self):
        to_visit = [self.root]
        while len(to_visit) > 0:
            cur_node = to_visit.pop(0)
            print(cur_node.payload)
            if cur_node.left is not None:
                to_visit.append(cur_node.left)
            if cur_node.right is not None:
                to_visit.append(cur_node.right)

    def dfs_rec(self):
        BinSearchTree.dfs(self.root)

    @staticmethod
    def dfs(node):
        if node.left is not None:
            BinSearchTree.dfs(node.left)
        if node.right is not None:
            BinSearchTree.dfs(node.right)

    def make_bst(self, arr):
        self.root = Node(int(arr.pop(0)))
        for elem in arr:
            BinSearchTree.add(self.root, int(elem))

        return self.root
