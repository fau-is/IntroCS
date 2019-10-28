import check50
import check50.c


@check50.check()
def compiles():
    """selsort.c compiles."""
    check50.c.compile("selsort.c", lcs50=True)


@check50.check(compiles)
def finds_usage():
    """returns usage without args"""
    check50.run("./selsort").stdout("Usage: ./bubble [asc|dsc]", regex=False).exit(1)
    check50.run("./selsort asdf").stdout("Usage: ./bubble [asc|dsc]", regex=False).exit(1)


@check50.check(compiles)
def sort_asc():
    """Does not ignore the prerequisites"""
    check50.run("./selsort asc").stdout("[2, 5, 8, 23, 33, 42, 78, 123, 2398, 4711]", regex=False).exit(0)


@check50.check(compiles)
def sort_dsc():
    """Does not ignore the prerequisites"""
    check50.run("./selsort dsc").stdout("[4711, 2398, 123, 78, 42, 33, 23, 8, 5, 2]", regex=False).exit(0)
