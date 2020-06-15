import check50
import check50.c

@check50.check()
def exists():
    """time.py"""
    check50.exists("time.py")

@check50.check(exists)
def compiles():
    """time.py compiles"""
    check50.c.compile("time.py", lcs50=True)

@check50.check(compiles)
def check():
    """time.py does what it is supposed to do"""
    check50.run("python time.py").stdout("Local: 06 / 15 / 2020, 10: 54:07").stdout("Montenegro is not in Trie")
