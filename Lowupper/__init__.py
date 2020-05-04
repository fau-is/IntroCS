import check50
import check50.c


@check50.check()
def exists_lowupper():
    """lowupper.c exists in WD."""
    check50.exists("lowupper.c")

@check50.check(exists_lowupper)
def compiles_lowupper():
    """lowupper.c compiles."""
    check50.c.compile("lowupper.c", lcs50=True)

@check50.check(compiles_lowupper)
def lower_upper():
    """print out new char array"""
    check50.run("./lowupper").stdout("[ a, B, c, D, e, F ]")
