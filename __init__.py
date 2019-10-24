import check50
import check50.c

@check50.check()
def compiles():
    """binary.c compiles."""
    check50.c.compile("binary.c", lcs50=True)

@check50.check(compiles)
def finds_10():
    """Finds 10 in the array"""
    check50.run("./binary 10").stdout("Number 10 is at index 0").exit(0)

@check50.check(compiles)
def finds_100():
    """Finds 10 in the array"""
    check50.run("./binary 100").stdout("Number 100 is at index 9").exit(0)

@check50.check(compiles)
def cannot_find_5():
    """Test not found message with 5"""
    check50.run("./binary 5").stdout("Number 5 not found").exit(1)
    
@check50.check(compiles)
def usage():
    """Check usage message"""
    check50.run("./binary").stdout("Usage: ./binary Number").exit(1)
