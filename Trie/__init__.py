import check50
import check50.c

@check50.check()
def exists():
    """tries.c exists."""
    check50.include("cities.txt")
    check50.exists("tries.c")

@check50.check(exists)
def compiles():
    """tries.c compiles."""
    check50.c.compile("tries.c", lcs50=True)

@check50.check(compiles)
def check():
    """trie is loaded successfully"""
    check50.run("./tries").stdout("Paris is not in Trie").stdout("Montenegro is not in Trie")
