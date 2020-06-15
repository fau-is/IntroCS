import check50
import check50.c

@check50.check()
def exists():
    """clean.py"""
    check50.include("silent_sea.txt")
    check50.include("silent_sea_clean.txt")
    check50.exists("clean.py")

@check50.check(exists)
def compiles():
    """clean.py compiles"""
    check50.c.compile("clean.py", lcs50=True)

@check50.check(compiles)
def check():
    """clean.py does what it is supposed to do"""
    check50.run("python clean.py").stdout("Paris is not in Trie").stdout("Montenegro is not in Trie")
