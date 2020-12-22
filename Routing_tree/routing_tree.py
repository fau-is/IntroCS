found = True

class BST:
    root = None
    def __init__(self, domain):
        self.domain = domain
        self.IP = None
        self.left = None
        self.right = None

    @staticmethod
    def add(domain, ip):
        if BST.root is None:
            BST.root = BST(domain)
            BST.root.IP = ip
        else:
            BST.add_recursion(BST.root, domain, ip)
    
    @staticmethod
    def add_recursion(cur_BST, value, IP):
        if cur_BST.domain < value:
            if cur_BST.right is not None:
                BST.add_recursion(cur_BST.right, value, IP)
            else:
                cur_BST.right = BST(value)
                cur_BST.right.IP = IP
        elif cur_BST.domain > value:
            if cur_BST.left is not None:
                BST.add_recursion(cur_BST.left, value, IP)
            else:
                cur_BST.left = BST(value)
                cur_BST.left.IP = IP
        else:
            return

    @staticmethod
    def find_question(to_find):
        cur_BST = BST.find(to_find)
        if cur_BST:
            print(to_find, '=', cur_BST.IP)
        else:
            print(to_find, 'does not exist in the Tree.')

    @staticmethod
    def find(to_find):
        if BST.root is not None:
            cur_BST = BST.find_recursion(BST.root, to_find)
            return cur_BST

    @staticmethod
    def find_recursion(cur_BST, to_find):
        if cur_BST is None:
            return
        elif cur_BST.domain == to_find:
            return cur_BST
        elif cur_BST.domain < to_find:
            return BST.find_recursion(cur_BST.right, to_find)
        elif cur_BST.domain > to_find:
            return BST.find_recursion(cur_BST.left, to_find)
        else:
            return

    @staticmethod
    def bfs():
        if BST.root is None:
            return
        BFS = []
        queue = []
        queue.append(BST.root)
        to_print = BST.bfs_recursive(queue, BFS)
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

            BST.bfs_recursive(queue, BFS)
        return BFS

    @staticmethod
    def preorder():
        List = []
        return BST.dfs_recursive(BST.root, List)

   
    @staticmethod
    def dfs_recursive(cur_BST, List):
        if cur_BST is not None:
            BST.dfs_recursive(cur_BST.left, List)
            List.append(cur_BST.domain)
            BST.dfs_recursive(cur_BST.right, List)
        return List

    @staticmethod
    def smallest_BST(cur_BST):
        current = cur_BST
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def deleteBST(root, domain):
        if root is None:
            return root

        if domain < root.domain:
            root.left = BST.deleteBST(root.left, domain)
        elif domain > root.domain:
            root.right = BST.deleteBST(root.right, domain)
        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = BST.smallest_BST(root.right)

            root.domain = temp.domain

            root.right = BST.deleteBST(root.right, temp.domain)

        return root

    @staticmethod
    def delete_method(domain):
        BST.root = BST.deleteBST(BST.root, domain)









