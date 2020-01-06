import check50
import check50.py

@check50.check()
def exists():
    """"runs"""
    check50.exists("dfs_gr.py")
    check50.include("dfs_gr_check.py")
    

@check50.check(exists)
def simple_test():
    """Simple Test"""
    check50.run("python3 dfs_gr_check.py").stdout("[0, 3, 4, 2]", regex=False).exit(0)

