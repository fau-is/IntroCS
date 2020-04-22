import check50
import check50.c

@check50.check()
def compiles_loops():
    """loops.c compiles."""
    check50.c.compile("loops.c", lcs50=True)

@check50.check()
def compiles_modulo():
    """modulo.c compiles."""
    check50.c.compile("modulo.c", lcs50=True)

@check50.check()
def compiles():
    """mario-1.c compiles."""
    check50.c.compile("mario-1.c", lcs50=True)

@check50.check()
def compiles():
    """mario-2.c compiles."""
    check50.c.compile("mario-2.c", lcs50=True)
