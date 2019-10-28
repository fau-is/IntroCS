import check50
import check50.c

@check50.check()
def compiles():
    """binary.c compiles."""
    check50.c.compile("binary.c", lcs50=True)

@check50.check(compiles)
def sorts_asc():
    """Finds 10 in the array"""
    check50.run("./binary 10").stdout("Number 10 is at index 0").exit(0)

@check50.check(compiles)
def sorts_dsc():
    """Finds 100 in the array"""
    check50.run("./binary 100").stdout("Number 100 is at index 9").exit(0)
    
@check50.check(compiles)
def usage():
    """Finds 50 in the array"""
    check50.run("./binary 50").stdout("Number 50 is at index 4").exit(1)
