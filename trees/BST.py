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
