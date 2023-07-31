import requests
import json
import sys
import graphviz
import os
import timeit
import time

# TODO: Fetching Followers
# 2.1 With authentication fetching followers of a specified id:
followers = set()
access_token = " N6-b43nxdfGzHU1BaMcUlFs39h1X3cCG2Bpv6WCPrZg "
id = "15530"

url = f"https://mastodon.social/api/v1/accounts/{id}/followers?limit=80"
while url:
    response = requests.get(url, headers={'Authorization':f'Bearer {access_token}'})
    objects = json.loads(response.text) # this converts the json to a python list of dictionary
    usernames = set([i['username'] for i in objects])
    followers |= usernames
    url = response.links['next']['url'] if 'next' in response.links else None

print(len(followers))
# for i in followers:
#     print(i)


def get_min(node):
    order = []
    queue = []
    queue.append(node)
    min_node = node

    while len(queue) > 0:
        thisNode = queue.pop()
        if thisNode.username in order:
            continue
        order.append(thisNode.username)
        if thisNode.username < min_node.username:
            min_node = thisNode
        if thisNode.right is not None:
            queue.append(thisNode.right)
        if thisNode.left is not None:
            queue.append(thisNode.left)

    return min_node

def draw_vertices(g, root):
    if root == None:
        return
    g.node(root.username,root.username)
    draw_vertices(g,root.left)
    draw_vertices(g, root.right)
    return

def draw_edges(g, root):
    if root == None:
        return
    if root.left != None:
        g.edge(root.username,root.left.username)
        draw_edges(g, root.left)
    if root.right != None:
        g.edge(root.username,root.right.username)
        draw_edges(g, root.right)
    return


def print_tree(root):
    g = graphviz.Graph(format='png', strict=True, filename='tree')
    draw_vertices(g, root)
    draw_edges(g, root)
    # graph.node(root.left, root.left)
    # graph.node(root.right, root.right)
    #
    # for n in g.keys():
    #     for t, w in g[n]:
    #         graph.edge(n, t, label=str(w))
    g.render()
    os.remove('tree')


class BST:
    """
    Class that represents our Binary Search Tree. We will use it to store followers.
    """

    # The root node of the BST
    root = None

    def __init__(self, username):
        """
        Constructor of the BST objects
        :param username: The username to be stored in an BST object
        """
        self.username = username
        self.left = None
        self.right = None

    @staticmethod
    def add(username):
        """
        The method creates a root if the BST does not have one yet, otherwise it adds a new BST object at the right
        place in the tree
        :param domain: The username of the added node (vertex)
        :return:
        """
        if BST.root is None:
            BST.root = BST(username)
        else:
            parent = BST.root
            if username < BST.root.username:
                child = BST.root.left
                left_pos = True
            else:
                child = BST.root.right
                left_pos = False
            while child is not None:
                if username < child.username:
                    parent = child
                    child = child.left
                    left_pos = True
                else:
                    parent = child
                    child = child.right
                    left_pos = False
            if left_pos:
                parent.left = BST(username)
            else:
                parent.right = BST(username)

    @staticmethod
    def find(to_find):
        CurNode = BST.root
        while CurNode is not None:
            if CurNode.username == to_find:
                return CurNode
            elif CurNode.username < to_find:
                CurNode = CurNode.right
            else:
                CurNode = CurNode.left
        return False

    # Recursive
    @staticmethod
    def search(root, key):

        # Base Cases: root is null or key is present at root
        if root is None or root.username == key:
            return root

        # Key is greater than root's key
        if root.username < key:
            return BST.search(root.right,key)

        # Key is smaller than root's key
        return BST.search(root.left,key)

    @staticmethod
    def bfs():
        """
        This method is supposed to perform a bfs
        :return: a list of the traversed elements as (preorder) BFS
        """
        order = []
        queue = []
        queue.append(BST.root)

        while len(queue) > 0:
            CurNode = queue.pop(0)
            if CurNode.username in order:
                continue
            order.append(CurNode.username)
            if CurNode.left is not None:
                queue.append(CurNode.left)
            if CurNode.right is not None:
                queue.append(CurNode.right)
        return order

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
    def delete_method(username):
        """Locate an element by its domain in the BST, if it exists, delete it"""
        CurNode = BST.root
        found = False
        while CurNode is not None:
            if CurNode.username == username:
                found = True
                break
            elif CurNode.username < username:
                is_left = False
                parent = CurNode
                CurNode = CurNode.right
            else:
                is_left = True
                parent = CurNode
                CurNode = CurNode.left

        if found:
            if CurNode.left is None and CurNode.right is None:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            elif CurNode.left is None and CurNode.right is not None:
                if is_left:
                    parent.left = CurNode.right
                else:
                    parent.right = CurNode.right
            elif CurNode.left is not None and CurNode.right is None:
                if is_left:
                    parent.left = CurNode.left
                else:
                    parent.left = CurNode.left
            else:
                min_cpy = get_min(CurNode.right)
                temp_user = min_cpy.username
                BST.delete_method(min_cpy.username)
                CurNode.username = temp_user
        else:
            return False

if __name__ == '__main__':
    # TODO: 1. Implement a binary search tree class, that stores all the followers of a user alphabetically. Implement the recursive binary search algorithm to check wether a username is listed in the user tree.
    for user in followers:
        BST.add(user)
    # iterative
    # found = BST.find("alextee")
    # if found:
    #     print(found.username, "is among the followers")
    # else:
    #     print("user was not found among the users.")

    # recursive
    found = BST.search(BST.root, "alextee")
    if found:
        print(found.username, "is among the followers.")
    else:
        print("user was not found among the users.")

    # TODO: 2. In order to display all of the followers, use the DFS algorithm from the previous exercise and make slight changes to it, such that it can traverse over the tree in a Pre-, In-, and Postorder.
    print('DFS (preorder): ', BST.preorder())
    print_tree(BST.root)
    # TODO: 3. Implement another suitable data structure of your choice, e.g. hash-table, trie, avl-tree, parse the followers onto it and compare the runtime for searching using pythons time library.
    to_find = "xolotl"
    # Data structure List: Linear search
    data_list = BST.preorder()
    def linear_search(data, find):
        for user in data:
            if user == find:
                return True
        return False
    exec_time = timeit.repeat(lambda: linear_search(data_list,to_find), number=100)
    print(f"user was found using linear search in {sum(exec_time)/len(exec_time)} seconds.")

    # Data structure BST: Binary search
    exec_time = timeit.repeat(lambda:BST.search(BST.root, to_find), number=100)
    print(f"user was found using binary search in {sum(exec_time)/len(exec_time)} seconds.")


#TODO: Find a more efficient data structure that beats our BST implementation as a task for students

