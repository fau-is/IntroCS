import check50


@check50.check()
def exists():
    """"runs"""
    check50.exists("bin_search_tree.py")
    check50.include("Printer.py")
    check50.include("Node.py")
    check50.include("bin_tree_check.py")
    

@check50.check(exists)
def example():
    """Example from PSet"""
    check50.run("python3 bin_tree_check.py 1,2,3,4,5,6,7,8").stdout("preorder: 1, 2, 3, 4, 5, 6, 7, 8, inorder: 1, 2, 3, 4, 5, 6, 7, 8, postorder: 8, 7, 6, 5, 4, 3, 2, 1, find 5: <Node.Node object at 0x11d3ac850>preorder: 3, inorder: 3, postorder: 3, find 5: None", regex=False).exit(0)


@check50.check(exists)
def small_tree():
    """Creates smaller tree"""
    check50.run("python3 bin_tree_check.py 3,4,6,2,1,9").stdout("preorder: 3, 2, 1, 4, 6, 9, inorder: 1, 2, 3, 4, 6, 9, postorder: 1, 2, 9, 6, 4, 3, find 5: Nonepreorder: 3, inorder: 3, postorder: 3, find 5: None", regex=False).exit(0)


@check50.check(exists)
def doubles():
    """Checks if no element is added multiple times"""
    check50.run("python3 bin_tree_check.py 3,4,6,2,1,9,3,4,6,2,1,9").stdout("preorder: 3, 2, 1, 4, 6, 9, inorder: 1, 2, 3, 4, 6, 9, postorder: 1, 2, 9, 6, 4, 3, find 5: Nonepreorder: 3, inorder: 3, postorder: 3, find 5: None", regex=False).exit(0)


@check50.check(exists)
def big_tree():
    """Add a lot"""
    check50.run("python3 bin_tree_check.py 3,4,6,2,1,9,9,4,65,91,4,1,0,34,67,2,5").stdout("preorder: 3, 2, 1, 0, 4, 6, 5, 9, 65, 34, 91, 67, inorder: 0, 1, 2, 3, 4, 5, 6, 9, 34, 65, 67, 91, postorder: 0, 1, 2, 5, 34, 67, 91, 65, 9, 6, 4, 3, find 5: <Node.Node object at 0x10f7e0410>preorder: 3, inorder: 3, postorder: 3, find 5: None", regex=False).exit(0)
