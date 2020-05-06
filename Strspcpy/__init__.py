import check50
import check50.c


@check50.check()
def compiles():
    """strspcpy.c compiles."""
    check50.c.compile("strspcpy.c")


@check50.check(compiles_lowupper)
def check_copy():
    """Can print 3 to 10 characters repetitively"""
    check50.run("./strspcpy 10 abc").stdout("abcabcabca?\n")


@check50.check(compiles_lowupper)
def check_copy_small():
    """Can copy a large string into a small output"""
    check50.run("./strspcpy 1 abc").stdout("a?\n")


@check50.check(compiles_lowupper)
def check_copy_same_size():
    """Can replicate the string exactly"""
    check50.run("./strspcpy 3 abc").stdout("abc?\n")

