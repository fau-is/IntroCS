---
files: [tree.py]
window: [terminal]
---
# TreeBuilder
## Lab Setup

Before we start hacking, you need to execute a few commands:

```
sudo apt install graphviz

pip install graphviz
```

If prompted whether you want to use up more space just type 'y' and hit Enter. Don't worry about any warnings.

## Task
In the class _BinTreeNode_, you need to implement the methods:
* _get\_min\_height\_free\_spot_ which returns the highest height of the next free child-tree.
* _add\_node_ which adds a node to a binary tree at the highest free spot.
    * When setting up a tree solely with _add\_node_ the resulting tree should always be left complete.

## Background information
* The task would be simpler if searching for the lowest depth in a sub-tree, however, if you would want to create an AVL-Tree you would need to compute the height. If you feel more comfortable doing that, just do it like that.
* Left complete: A tree is filled to the leaf level and starts from the left to fill up the leaf-level.
* In any tree-based data structure, Recursion is your friend.

Python provides a built_in function _min()_ which returns the minimum of all compared values.

## Test Your Code
Feel free to use the test_tree.py file to test your Code.


