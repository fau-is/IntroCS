import check50
import check50.c

@check50.check()
def exists_inverse():
    """inverse.c exists in WD."""
    check50.exists("inverse.c")

@check50.check(exists_inverse)
def compiles_inverse():
    """inverse.c compiles."""
    check50.c.compile("inverse.c", lcs50=True)

@check50.check(compiles_inverse)
def two_argc():
    """only allows 2 cmd line argmuents"""
    check50.run("./inverse Hello Hello").stdout("Input word\n")
    check50.run("./inverse").stdout("Input word\n")
    
@check50.check(compiles_inverse)
def inverse_isalpha():
    """re-prompts on non alphabetical input"""
    check50.run("./inverse H1llo").stdout("Input word\n")

@check50.check(compiles_inverse)
def inverse_stdin():
    """print out inverse"""
    check50.run("./inverse scortni").stdout("introcs\n")
