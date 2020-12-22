found = True

class Node:
    root = None
    def __init__(self, domain):
        self.domain = domain
        self.IP = None
        self.left = None
        self.right = None

    @staticmethod
    def add(domain, ip):
        if Node.root is None:
            Node.root = Node(domain)
            Node.root.IP = ip
        else:
            Node.add_recursion(Node.root, domain, ip)
    
    @staticmethod
    def add_recursion(cur_node, value, IP):
        if cur_node.domain < value:
            if cur_node.right is not None:
                Node.add_recursion(cur_node.right, value, IP)
            else:
                cur_node.right = Node(value)
                cur_node.right.IP = IP
        elif cur_node.domain > value:
            if cur_node.left is not None:
                Node.add_recursion(cur_node.left, value, IP)
            else:
                cur_node.left = Node(value)
                cur_node.left.IP = IP
        else:
            return

    @staticmethod
    def find_question(to_find):
        cur_node = Node.find(to_find)
        if cur_node:
            print(to_find, '=', cur_node.IP)
        else:
            print(to_find, 'does not exist in the Tree.')

    @staticmethod
    def find(to_find):
        if Node.root is not None:
            cur_node = Node.find_recursion(Node.root, to_find)
            return cur_node

    @staticmethod
    def find_recursion(cur_node, to_find):
        if cur_node is None:
            return
        elif cur_node.domain == to_find:
            return cur_node
        elif cur_node.domain < to_find:
            return Node.find_recursion(cur_node.right, to_find)
        elif cur_node.domain > to_find:
            return Node.find_recursion(cur_node.left, to_find)
        else:
            return

    @staticmethod
    def bfs():
        if Node.root is None:
            return
        BFS = []
        queue = []
        queue.append(Node.root)
        to_print = Node.bfs_recursive(queue, BFS)
        print(to_print)
    
    @staticmethod
    def bfs_recursive(queue, BFS):
        if queue:
            current = queue[0]
            BFS.append(current.domain)
            queue.pop(0)
            if current.left:
                queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            elif current.right:
                queue.append(current.right)

            Node.bfs_recursive(queue, BFS)
        return BFS

    @staticmethod
    def print_preorder():
        print('[', end="")
        Node.dfs_recursive(Node.root)
        print(']')
   
    @staticmethod
    def dfs_recursive(cur_node):
        if cur_node is not None:
            Node.dfs_recursive(cur_node.left)
            print(cur_node.domain, ", ", end="")
            Node.dfs_recursive(cur_node.right)

    @staticmethod
    def smallest_node(cur_node):
        current = cur_node
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def deleteNode(root, domain):
        if root is None:
            return root

        if domain < root.domain:
            root.left = Node.deleteNode(root.left, domain)
        elif domain > root.domain:
            root.right = Node.deleteNode(root.right, domain)
        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = Node.smallest_node(root.right)

            root.domain = temp.domain

            root.right = Node.deleteNode(root.right, temp.domain)

        return root

    @staticmethod
    def delete_method(domain):
        Node.root = Node.deleteNode(Node.root, domain)









