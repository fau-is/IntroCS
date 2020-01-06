import check50


@check50.check()
def exists():
    """"runs"""
    check50.exists("bin_tree.py")
    check50.include("bin_tree_check.py")
    

@check50.check(exists)
def example():
    """Example from PSet"""
    check50.run("python3 bin_tree_check.py 1,2,3,4,5,6,7,8").stdout("preorder: 1, 2, 4, 8, 5, 3, 6, 7, inorder: 8, 4, 2, 5, 1, 6, 3, 7, postorder: 8, 4, 5, 2, 6, 7, 3, 1, ", regex=False).exit(0)


@check50.check(exists)
def small_tree():
    """Creates smaller tree"""
    check50.run("python3 bin_tree_check.py 3,4,6,2,1,9").stdout("preorder: 3, 4, 2, 1, 6, 9, inorder: 2, 4, 1, 3, 9, 6, postorder: 2, 1, 4, 9, 6, 3, ", regex=False).exit(0)


@check50.check(exists)
def big_tree():
    """Trees a lot"""
    check50.run("python3 bin_tree_check.py 3,4,6,2,1,9,9,4,65,91,4,1,0,34,67,2,5").stdout("preorder: 3, 4, 2, 4, 2, 5, 65, 1, 91, 4, 6, 9, 1, 0, 9, 34, 67, inorder: 2, 4, 5, 2, 65, 4, 91, 1, 4, 3, 1, 9, 0, 6, 34, 9, 67, postorder: 2, 5, 4, 65, 2, 91, 4, 1, 4, 1, 0, 9, 34, 67, 9, 6, 3, ", regex=False).exit(0)
