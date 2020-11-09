import check50
import check50.c


@check50.check()
def exists_modulo():
    """modulo.c exists in WD."""
    check50.exists("modulo.c")

@check50.check(exists_modulo)
def compiles_modulo():
    """modulo.c compiles."""
    check50.c.compile("modulo.c", lcs50=True)

@check50.check(compiles_modulo)
def even():
    """check for even number number"""
    check50.run("./modulo").stdin("2").stdout("2 is an even number.?\n", regex=True)

@check50.check(compiles_modulo)
def uneven():
    """check for uneven number"""
    check50.run("./modulo").stdin("3").stdout("3 is an uneven number.?\n", regex=True)

