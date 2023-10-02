class BST:
    """
    Class that represents our Binary Search Tree.
    """

    # The root node of the BST
    root = None

    def __init__(self, username):
        """
        Constructor of the BST objects.
        :param username: The username to be stored in a BST object.
        """
        self.username = username
        self.left = None
        self.right = None

    @staticmethod
    def add(username):
        """
        The method creates a root if the BST does not have one yet, otherwise it adds a new BST object at the right
        place in the tree.
        :param username: The username of the added node (vertex).
        :return:
        """
        if BST.root is None:
            BST.root = BST(username)
        else:
            BST._add_recursive(BST.root, username)

    @staticmethod
    def _add_recursive(current, username):
        """
        Recursive helper method for adding a new node.
        """
        if username < current.username:
            if current.left is None:
                current.left = BST(username)
            else:
                BST._add_recursive(current.left, username)
        elif username > current.username:
            if current.right is None:
                current.right = BST(username)
            else:
                BST._add_recursive(current.right, username)


    @staticmethod
    def linear_search(to_find):
        CurNode = BST.root
        while CurNode is not None:
            if CurNode.username == to_find:
                return CurNode
            elif CurNode.username < to_find:
                CurNode = CurNode.right
            else:
                CurNode = CurNode.left
        return False



    @staticmethod
    def binary_search(root, to_find):
        # Base Cases: root is null or key is present at root
        if root is None:
            return False
        if root is None or root.username == to_find:
            return root

        # Key is greater than root's key
        if root.username < to_find:
            return BST.binary_search(root.right,to_find)

        # Key is smaller than root's key
        return BST.binary_search(root.left,to_find)


    @staticmethod
    def preorder():
        """
        This method is supposed to perform preorder DFS.
        :return: a list of the domain names in preorder.
        """
        order = []
        queue = []
        queue.append(BST.root)

        while len(queue) > 0:
            CurNode = queue.pop()
            if CurNode.username in order:
                continue
            order.append(CurNode.username)
            if CurNode.right is not None:
                queue.append(CurNode.right)
            if CurNode.left is not None:
                queue.append(CurNode.left)
        return order

    @staticmethod
    def inorder():
        """
        This method performs inorder DFS.
        :return: a list of the domain names in inorder.
        """
        order = []
        stack = []
        CurNode = BST.root

        while CurNode is not None or len(stack) > 0:
            while CurNode is not None:
                stack.append(CurNode)
                CurNode = CurNode.left
            CurNode = stack.pop()
            order.append(CurNode.username)
            CurNode = CurNode.right

        return order

    @staticmethod
    def postorder():
        """
        This method performs postorder DFS.
        :return: a list of the domain names in postorder.
        """
        order = []
        stack1 = []
        stack2 = []
        stack1.append(BST.root)

        while len(stack1) > 0:
            CurNode = stack1.pop()
            stack2.append(CurNode)
            if CurNode.left is not None:
                stack1.append(CurNode.left)
            if CurNode.right is not None:
                stack1.append(CurNode.right)

        while len(stack2) > 0:
            node = stack2.pop()
            order.append(node.username)

        return order