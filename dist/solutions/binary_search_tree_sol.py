from typing import Tuple, List

class BST:
    """
    A class that represents a Binary Search Tree (BST).

    Attributes:
    ----------
    root: BST
        The root node of the BST.

    """

    # The root node of the BST
    root = None

    def __init__(self, username: str) -> None:
        """
        Constructor for the BST objects.

        Parameters:
        ----------
        username: str
            The username to be stored in a BST object.
        """
        self.username = username
        self.left = None
        self.right = None


    @staticmethod
    def add(username: str) -> None:
        """
        Creates a root if the BST does not have one yet, otherwise adds a new BST object at the right place in the tree.

        Parameters:
        ----------
        username: str
            The username of the added node (vertex).
        """
        if BST.root is None:
            BST.root = BST(username)
        else:
            BST._add_recursive(BST.root, username)

    @staticmethod
    def _add_recursive(current: 'BST', username: str) -> None:
        """
        Recursive helper method for adding a new node.

        Parameters:
        ----------
        current: BST
            The current node in the BST where the new node might be added.
        username: str
            The username of the new node.
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
    def linear_search(to_find: str) -> Tuple['BST', bool]:
        """
        Searches for a node in the BST using a linear approach.

        Parameters:
        ----------
        to_find: str
            The username to find in the BST.

        Returns:
        -------
        Union[BST, bool]
            The found BST node or False if not found.
        """
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
    def binary_search(root: 'BST', to_find: str) -> Tuple['BST', bool]:
        """
        Searches for a node in the BST using a binary search approach.

        Parameters:
        ----------
        root: BST
            The current root node for the binary search.
        to_find: str
            The username to find in the BST.

        Returns:
        -------
        Union[BST, bool]
            The found BST node or False if not found.
        """
        if root is None:
            return False
        if root.username == to_find:
            return root

        # Key is greater than root's key
        if root.username < to_find:
            return BST.binary_search(root.right, to_find)

        # Key is smaller than root's key
        return BST.binary_search(root.left, to_find)

    @staticmethod
    def preorder() -> List[str]:
        """
        Performs a preorder Depth-First Search (DFS) on the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in preorder.
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
    def inorder() -> List[str]:
        """
        Performs an inorder Depth-First Search (DFS) on the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in inorder.
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
    def postorder() -> List[str]:
        """
        Performs a postorder Depth-First Search (DFS) on the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in postorder.
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
