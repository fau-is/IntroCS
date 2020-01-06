import check50
import dfs_gr_check as dfsc


@check50.check()
def exists():
    """"runs"""
    check50.exists("dfs_gr.py")
    

@check50.check()
def simple_test():
    """Simple Test"""
    check50.check()
    check50.run("python3 dfs_gr_check.py").stdout("[0, 3, 4, 2]", regex=False).exit(0)

    from re import match

    expected = "[0, 3, 4, 2]"
    actual = dfsc.main
    if not match(expected, actual):
        raise check50.Mismatch("hello, world\n", actual)
