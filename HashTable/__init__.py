import check50
import check50.c

@check50.check()
def exists():
    """hashtable.c exists."""
    check50.exists("hashtable.c")

@check50.check(exists)
def compiles():
    """hashtable.c compiles."""
    check50.c.compile("hashtable.c", lcs50=True)

@check50.check(compiles)
def check():
    """hashtable prints successfully"""
    check50.run("./hashtable").stdout("Chris exists").stdout("Tobias does not exist")
