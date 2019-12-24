from Node import Node


class BST:

    def __init__(self, arr):
        if arr is None or len(arr) < 1:
            self.root = None
        else:
            self.root = None
            self.root = self.make_bst(arr)

    def make_bst(self, arr):
        self.root = Node(int(arr.pop(0)))
        for elem in arr:
            BST.add_helper(self.root, int(elem))

        return self.root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            BST.add_helper(self.root, value)

    @staticmethod
    def add_helper(root, value):
        if root.payload < value:
            if root.right is None:
                root.right = Node(value)
            else:
                BST.add_helper(root.right, value)
        elif root.payload > value:
            if root.left is None:
                root.left = Node(value)
            else:
                BST.add_helper(root.left, value)
        else:
            return

    def delete(self, value):
        self.root = BST.delete_helper(self.root, value)

    @staticmethod
    def delete_helper(root, value):
        if root is None:
            return root
        # find the right node that is to be deleted
        if value < root.payload:
            root.left = BST.delete_helper(root.left, value)
        elif value > root.payload:
            root.right = BST.delete_helper(root.right, value)
        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # determine the new value of root
            root.payload = BST.min_finder(root.right).payload

            # delete the redundant value
            root.right = BST.delete_helper(root.right, root.payload)

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
            # print(cur_node.payload)
            if cur_node.left is not None:
                to_visit.append(cur_node.left)
            if cur_node.right is not None:
                to_visit.append(cur_node.right)

    def find(self, value):
        return BST.find_helper(self.root, value)

    @staticmethod
    def find_helper(root, value):
        if root is None or root.payload == value:
            return root
        elif root.payload < value:
            return BST.find_helper(root.right, value)
        else:
            return BST.find_helper(root.left, value)



    def dfs_rec(self):
        BST.dfs(self.root)

    @staticmethod
    def dfs(node):
        if node.left is not None:
            BST.dfs(node.left)
        if node.right is not None:
            BST.dfs(node.right)
