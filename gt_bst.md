# UserTree

In our digital age, social networks play a significant role in connecting people worldwide. When you follow someone on a platform, your action isn't merely a click. In the background, algorithms and data structures manage and organize this vast amount of information. One such foundational structure is the Binary Search Tree (BST).

BST is a hierarchical structure that maintains order, enabling efficient searching, insertion, and deletion operations. In this exercise, we will leverage the power of BSTs to manage and search through followers of a user on a the Mastodon social platform.

Your task is to construct this BST, ensuring that each follower is stored alphabetically, making search operations swift and efficient.



## Getting Started

Log into the [CS50 IDE](https://cs50.dev/) and follow these steps:

1. Execute `cd` to ensure that you're in `~/` (i.e., your home directory).
2. Execute `mkdir Graphs_Trees` to create a directory named `Graphs_Trees`.
3. Navigate into your newly created directory with `cd Graphs_Trees`.
4. Download the starter code: `wget https://introcs.is.rw.fau.de/assets/pdfs/mastodon_tree.zip`.
5. Extract the starter code: `unzip follower_tree.zip`.
6. Clean up by deleting the ZIP file: `rm follower_tree.zip` and confirm with `yes` or `y`.
7. Execute `ls`. You should see this problem's distribution: `follower_tree.py` and `binary_search_tree.py`.

**You only have to code in `binary_search_tree.py`. You can use `follower_tree.py` to test and debug your binary search tree implementation.**


## Specification

Your goal is to craft a Binary Search Tree (BST) that organizes followers alphabetically and provides swift search capabilities.


### 1. Binary Search Tree (BST) Creation

Design and implement a BST that stores followers of a user in an alphabetical manner. For this task:
* Each node should have a maximum of two children: left and right.
* If a follower's name is alphabetically less than the current node, it should reside in the left subtree. If it's greater, it should be on the right.





We provided you the file binary_search_tree.py. For task 1 complete the constructor as well as the method add().

- **BST Class**: This class represents the Binary Search Tree.
  - **root**: A class-level attribute that keeps track of the starting point or the root of our BST. Initially, it's set to `None`, indicating an empty tree.
  - **Constructor (`__init__`)**: Every time you create a new instance of the BST class, this constructor will be called. It expects a `username` as its parameter, which represents the username to be stored in that particular BST node.
  - **add() Method**: This static method will allow us to add new usernames to our tree. If the tree is empty (i.e., `root` is `None`), the method will set the new username as the root. Otherwise, it will find the appropriate location in the tree to add the new username such that the BST property (left children are less than the parent and right children are greater than the parent) is maintained.

Hint: To find the appropriate location in the tree, we recommend using recursion. You can of course add helper methods to your class. However, it is also possible without recursion and additional methods.

---


### 2. Search (linear & binary)

* Implement a search algorithm to determine if a username exists in the BST.
* Provide both a linear and a binary implementation in its respective function.
* The search should return the Node if the username is found, and `False` otherwise.


Hint: When you see -> Union[] in a function signature, it's used in conjunction with Python's typing module to indicate that the function can return values of different types. The Union type is used to specify that the return value can be one of several types. For example, Union['BST', False] means the function can return either a binary search tree or a the bool False.
***

### 3. Depth-First Search (DFS) Modifications

Using your DFS knowledge from the previous exercise:

* Modify the DFS algorithm to traverse the BST.
* Implement functions for three types of tree traversals:
  * **Preorder**: Visit the current node before its child nodes.
  * **Inorder**: Visit the left child, then the current node, and finally the right child.
  * **Postorder**: Visit the child nodes first, then the current node.

Remember, the traversal order is crucial for different applications. For instance, the inorder traversal in a BST will give you the followers in alphabetical order!





***

# check50

After implementing, you can validate your solution with:

```
check50 fau-is/IntroCS/PyBSTFollowers/Follower_tree
```

# submit50

To submit your solution:

```
submit50 fau-is/IntroCS/PyBSTFollowers/Follower_tree
```

Good luck, and enjoy the process of bringing order to the vast world of followers!