import check50
import check50.c

@check50.check()
def compiles():
    """m_bubble.c compiles."""
    check50.c.compile("m_bubble.c", lcs50=True)

@check50.check(compiles)
def sorts_asc():
    """Finds 10 in the array"""
    check50.run("./bubble asc").stdout("[2, 5, 8, 23, 33, 42, 78, 123, 2398, 4711]").exit(0)

@check50.check(compiles)
def sorts_dsc():
    """Finds 100 in the array"""
    check50.run("./bubble dsc").stdout("[4711, 2398, 123, 78, 42, 33, 23, 8, 5, 2]").exit(0)
    
@check50.check(compiles)
def usage():
    """Finds 50 in the array"""
    check50.run("./bubble ots").stdout("Usage: ./bubble [asc|dsc]\n").exit(1)
