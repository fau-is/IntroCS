import check50
import check50.c

#multiply:

@check50.check()
def exists_multiply():
    """mario-2.c exists in WD."""
    check50.exists("multiply.c")

@check50.check(multiply)
def compiles_mario_2():
    """mario-2.c compiles."""
    check50.c.compile("multiply", lcs50=True)


