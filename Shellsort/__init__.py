import check50
import check50.c


@check50.check()
def exists_shellsort():
    """stupidsort.c exists in WD."""
    check50.exists("shellsort.c")


@check50.check(exists_shellsort)
def compiles_shellsort():
    """stupidsort.c compiles."""
    check50.c.compile("shellsort.c", lcs50=True)


@check50.check(compiles_shellsort)
def shellsort_sorts():
    """The sorting algorithm sorts"""
    check50.run("./shellsort").stdout("[ 1, 2, 3, 3, 4, 5, 6, 7, 8, 10 ]")
