import check50
import check50.c

#multiply:

@check50.check()
def exists_multiply():
    """multiply.c exists in WD."""
    check50.exists("multiply.c")

@check50.check(exists_multiply)
def compiles():
    """multiply compiles."""
    check50.c.compile("multiply", lcs50=True)

@check50.check(compiles)
def multiplies():
    """multiply does what it is supposed to do."""
    check50.run("./multiply").stdin("1").stdout("[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]")


