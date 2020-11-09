import check50
import check50.c

#getint:

@check50.check()
def exists_getint():
    """mario-1.c exists in WD."""
    check50.exists("getint.c")

@check50.check(exists_getint)
def compiles_getint():
    """mario-1.c compiles."""
    check50.c.compile("getint.c", lcs50=True)

@check50.check(compiles_getint)
def output_getint():
    """Input Number is between 0 and 100 inclusively"""
    check50.run("./getint").stdin("50").stdout("Nice! the input Number was: 50\n")
    check50.run("./getint").stdin("120").stdout("Nope! the input Number was: 120\n")



