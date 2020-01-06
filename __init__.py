import check50


@check50.check()
def exists():
    """"runs"""
    check50.exists("avl.py")
    check50.include("Printer.py")
    check50.include("bin_tree_check_0.py")
    check50.include("bin_tree_check_1.py")
    check50.include("bin_tree_check_2.py")
    

@check50.check(compiles)
def test_ez():
    """example:
            30
           /  \
         20   40
        /  \     \
       10  25    50"""
    check50.run("python3 bin_tree_check_0.py")\
        .stdout("10, 20, 25, 30, 40, 50, 30, 20, 10, 25, 40, 50, 10, 25, 20, 50, 40, 30, "
                , regex=False).exit(0)

@check50.check(compiles)
def test_0_9():
    """test with insert 0-9"""
    check50.run("python3 bin_tree_check_1.py")\
        .stdout("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 3, 2, 1, 5, 4, 9, 8, 7, 10, 1, 2, 4, 5, 3, 7, 8, 10, 9, 6, "
                , regex=False).exit(0)
    
@check50.check(compiles)
def doubles():
    """test double values"""
    check50.run("python3 bin_tree_check_2.py")\
        .stdout("-3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 1, -3, 3, 2, 4, 8, 7, 6, 9, -3, 2, 4, 3, 1, 6, 7, 9, 8, 5, "
                , regex=False).exit(0)
