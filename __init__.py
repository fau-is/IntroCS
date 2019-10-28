import check50
import check50.c

@check50.check()
def compiles():
    """bubble.c compiles."""
    check50.c.compile("bubble.c", lcs50=True)

@check50.check(compiles)
def sorts_asc():
    """Sorts ascending"""
    check50.run("./bubble asc").stdout("[2, 5, 8, 23, 33, 42, 78, 123, 2398, 4711]").exit(0)

@check50.check(compiles)
def sorts_dsc():
    """Sorts descending"""
    check50.run("./bubble dsc").stdout("[4711, 2398, 123, 78, 42, 33, 23, 8, 5, 2]").exit(0)
    
@check50.check(compiles)
def usage():
    """Prints Usage"""
    check50.run("./bubble ots").stdout("Usage: ./bubble [asc|dsc]").exit(1)
