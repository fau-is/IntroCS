import check50
import check50.c

#Loops:

@check50.check()
def exists_loops():
    """loops.c exists in WD."""
    check50.exists("loops.c")

@check50.check(exists_loops)
def compiles_loops():
    """loops.c compiles."""
    check50.c.compile("loops.c", lcs50=True)

#Modulo:

@check50.check()
def exists_modulo():
    """modulo.c exists in WD."""
    check50.exists("modulo.c")

@check50.check(exists_modulo)
def compiles_modulo():
    """modulo.c compiles."""
    check50.c.compile("modulo.c", lcs50=True)

#Mario-1:

@check50.check()
def exists_mario_1():
    """mario-1.c exists in WD."""
    check50.exists("mario-1.c")

@check50.check(exists_mario_1)
def compiles_mario_1():
    """mario-1.c compiles."""
    check50.c.compile("mario-1.c", lcs50=True)

#Mario-2:

@check50.check()
def exists_mario_2():
    """mario-2.c exists in WD."""
    check50.exists("mario-2.c")

@check50.check(exists_mario_2)
def compiles_mario_2():
    """mario-2.c compiles."""
    check50.c.compile("mario-2.c", lcs50=True)
