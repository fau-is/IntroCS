class BST:
    """
    Class that represents our Binary Search Tree. We will use it to mimic a Domain Name System.
    """

    # The root node of the BST
    root = None

    def __init__(self, domain, ip):
        """
        Constructor of the BST objects
        :param domain: The domain to be stored in an BST object
        :param ip: The domain's respective IP address
        """
        self.domain = domain
        self.IP = ip
        self.left = None
        self.right = None

    @staticmethod
    def add(domain, ip):
        """
        The method creates a root if the BST does not have one yet, otherwise it adds a new BST object at the right
        place in the tree
        :param domain: The domain name of the added node (vertex)
        :param ip: The ip of the domain to be added
        :return:
        """
        # TODO
        pass

    @staticmethod
    def find(to_find):
        # TODO
        return False

    @staticmethod
    def bfs():
        """
        This method is supposed to perform a bfs
        :return: a list of the traversed elements as (preorder) BFS
        """
        order = []
        # TODO
        return order

    @staticmethod
    def preorder():
        """
        This method is supposed to perform preorder DFS.
        :return: a list of the domain names in preorder.
        """
        order = []
        # TODO
        return order


    @staticmethod
    def delete_method(domain):
        """Locate an element by its domain in the BST, if it exists, delete it"""
        # TODO
        pass





