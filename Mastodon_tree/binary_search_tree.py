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



    @staticmethod
    def add(username: str) -> None:
        """
        Creates a root if the BST does not have one yet, otherwise adds a new BST object at the right place in the Mastodon_tree.

        Parameters:
        ----------
        username: str
            The username of the added node (vertex).
        """


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
        Tuple[BST, bool]
            The found BST node or False if not found.
        """



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
        Tuple[BST, bool]
            The found BST node or False if not found.
        """


    @staticmethod
    def preorder() -> List[str]:
        """
        Performs a preorder Depth-First Search (DFS) on the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in preorder.
        """


    @staticmethod
    def inorder() -> List[str]:
        """
        Performs an inorder Depth-First Search (DFS) on the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in inorder.
        """


    @staticmethod
    def postorder() -> List[str]:
        """
        Performs a postorder Depth-First Search (DFS) on the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in postorder.
        """

