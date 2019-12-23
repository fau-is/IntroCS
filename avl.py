from Node import Node


# AVL tree class which supports the
# Insert operation
class avl_tree(object):

    # ret new root
    def insert(self, root, value):

        # Step 1 - BST search
        if not root:
            return Node(value)
        elif value < root.payload:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # Step 2 - Update height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - Get balance factor
        balance = self.getBalance(root)

        # Step 4 - Rebalancing
        # Case 1 - right rotation
        if balance > 1 and value < root.left.payload:
            return self.rightRotate(root)

        # Case 2 - left rotation
        if balance < -1 and value > root.right.payload:
            return self.leftRotate(root)

        # Case 3 - left right rotation
        if balance > 1 and value > root.left.payload:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - right left rotation
        if balance < -1 and value < root.right.payload:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # returns new root
    def delete(self, root, value):

        # Step 1 - BST del
        if not root:
            return root

        elif value < root.val:
            root.left = self.delete(root.left, value)

        elif value > root.val:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                     temp.val)

        # only one node
        if root is None:
            return root

        # Step 2 - update height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - get balance factor
        balance = self.getBalance(root)

        # Step 4 - rebalancing
        # Case 1 - right rotation
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Case 2 - left rotation
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Case 3 - left right rotation
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - right left rotation
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return -1

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def inorder(self, root):

        if not root:
            return

        self.inorder(root.left)
        print("{0} ".format(root.payload), end="")
        self.inorder(root.right)

    # Driver program to test above function


myTree = avl_tree()
root = None

root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

"""The constructed AVL Tree would be 
			30 
		/ \ 
		20 40 
		/ \	 \ 
	10 25 50"""

# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
myTree.inorder(root)
print()

# This code is contributed by Ajitesh Pathak
