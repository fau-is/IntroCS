import check50
import check50.py

@check50.check()
def exists():
    """"runs"""
    check50.exists("dfs_gr.py")
    check50.include("dfs_gr_check.py")
    check50.py.append_code("dfs_gr.py","dfs_gr_check.py")
    

@check50.check(exists)
def simple_test():
    """Simple Test"""
    # check50.check()
    # check50.run("python3 dfs_gr_check.py").stdout("[0, 3, 4, 2]", regex=False).exit(0)

    from re import match

    expected = "[0, 3, 4, 2]"
    actual = main()
    if not match(expected, actual):
        raise check50.Mismatch("hello, world\n", actual)
#     graph = Graph([[1,2,3],[3,4],[4],[4],[]])
#     nbr, path = graph.dfs(0, 2)
#     return path
