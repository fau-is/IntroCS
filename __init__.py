import check50
import check50.c

@check50.check()
def compiles():
    """linear.c compiles."""
    check50.c.compile("linear.c", lcs50=True)

@check50.check(compiles)
def finds_1():
    """Finds 1 in the array"""
    check50.run("./linear 1").stdout("Number 1 is at index 0").exit(0)

@check50.check(compiles)
def finds_11():
    """Finds 11 in the array"""
    check50.run("./linear 11").stdout("Number 11 is at index 2").exit(0)
    
@check50.check(compiles)
def finds_4():
    """Finds 4 in the array"""
    check50.run("./linear 4").stdout("Number 4 is at index 3").exit(0)
    
@check50.check(compiles)
def finds_7():
    """Finds 7 in the array"""
    check50.run("./linear 7").stdout("Number 7 is at index 9").exit(0)

@check50.check(compiles)
def cannot_find_3():
    """Test not found message with 3"""
    check50.run("./linear 3").stdout("Number 3 not found").exit(1)
    
@check50.check(compiles)
def usage():
    """Check usage message"""
    check50.run("./linear").stdout("Usage: ./linear Number").exit(1)
