import check50


@check50.check()
def exists():
    """"runs"""
    check50.exists("dfs_gr.py")
    

@check50.check(compiles)
def simple_test():
    """Simple Test"""
    check50.run("python3 dfs_gr_check.py").stdout("[0, 3, 4, 2]", regex=False).exit(0)
