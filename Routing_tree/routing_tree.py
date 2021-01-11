class BST:
    root = None

    def __init__(self, domain, ip):
        self.domain = domain
        self.IP = ip
        self.left = None
        self.right = None

    @staticmethod
    def add(domain, ip):
        if BST.root is None:
            BST.root = BST(domain, ip)
        else:
            BST.root = BST.add_recursion(BST.root, domain, ip)

    @staticmethod
    def add_recursion(node, domain, ip):
        if node is None:
            return BST(domain, ip)
        else:
            if node.domain < domain:
                node.right = BST.add_recursion(node.right, domain, ip)
            else:
                node.left = BST.add_recursion(node.left, domain, ip)
        return node

    @staticmethod
    def find(to_find):
        stack = [BST.root]
        while stack:
            cur_node = stack.pop(0)
            if cur_node.domain == to_find:
                return cur_node
            else:
                if cur_node.domain < to_find and cur_node.right is not None:
                    stack.append(cur_node.right)
                elif cur_node.left is not None:
                    stack.append(cur_node.left)

        return False


    @staticmethod
    def bfs():
        stack = []
        order = []
        cur_node = BST.root
        stack.append(cur_node)
        while len(stack) > 0:
            cur_node = stack.pop(0)
            if cur_node.left is not None:
                stack.append(cur_node.left)
            if cur_node.right is not None:
                stack.append(cur_node.right)
            order.append(cur_node.domain)

        return order

    @staticmethod
    def preorder():
        """
        This method is supposed to perform preorder DFS.
        :return: a list of the domain names in the preorder order.
        """
        # TODO
        return BST.preorder_helper(BST.root, [])

    @staticmethod
    def preorder_helper(node, order):
        if node is not None:
            order.append(node.domain)
            order = BST.preorder_helper(node.left, order)
            order = BST.preorder_helper(node.right, order)
        return order

    @staticmethod
    def delete_method(domain):
        BST.root = BST.deleteNode(BST.root, domain)

    @staticmethod
    def smallest_node(cur_node):
        current = cur_node
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def deleteNode(node, domain):
        if node is None:
            return node

        if domain < node.domain:
            node.left = BST.deleteNode(node.left, domain)
        elif domain > node.domain:
            node.right = BST.deleteNode(node.right, domain)
        else:

            if node.left is None:
                temp = node.right
                root = None
                return temp

            elif node.right is None:
                temp = node.left
                root = None
                return temp

            temp = BST.smallest_node(node.right)

            node.domain = temp.domain

            node.right = BST.deleteNode(node.right, temp.domain)

        return node




