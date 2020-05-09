import check50
import check50.c


@check50.check()
def exists_stupidsort():
    """stupidsort.c exists in WD."""
    check50.exists("stupidsort.c")


@check50.check(exists_stupidsort)
def compiles_stupidsort():
    """stupidsort.c compiles."""
    check50.c.compile("stupidsort.c", lcs50=True)


@check50.check(compiles_stupidsort)
def stupidsort_sorts():
    """The sorting algorithm sorts"""
    check50.run("./stupidsort").stdout("[ 1, 2, 3, 4, 5, 6, 7, 8, 10 ]")
