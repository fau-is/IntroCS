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

@check50.check(compiles_loops)
def prints_output():
    """Prints output equal to default"""
    check50.run("./loops").stdout("i = 0, j = 0\ni = 0, j = 1\ni = 0, j = 2\ni = 0, j = 3\ni = 0, j = 4\ni = 1, j = 0\ni = 1, j = 1\ni = 1, j = 2\ni = 1, j = 3\ni = 1, j = 4\ni = 2, j = 0\ni = 2, j = 1\n"\
    +"i = 2, j = 2\ni = 2, j = 3\ni = 2, j = 4\ni = 3, j = 0\ni = 3, j = 1\ni = 3, j = 2\ni = 3, j = 3\ni = 3, j = 4\ni = 4, j = 0\ni = 4, j = 1\ni = 4, j = 2\ni = 4, j = 3\ni = 4, j = 4")

#Modulo:

@check50.check()
def exists_modulo():
    """modulo.c exists in WD."""
    check50.exists("modulo.c")

@check50.check(exists_modulo)
def compiles_modulo():
    """modulo.c compiles."""
    check50.c.compile("modulo.c", lcs50=True)

@check50.check(compiles_modulo)
def even_uneven():
    """check for even number and uneven number"""
    check50.run("./modulo").stdin("2").stdout("2 is an even number!\n").run("./modulo").stdin("3").stdout("3 is an uneven number!\n")

#Mario-1:

@check50.check()
def exists_mario_1():
    """mario-1.c exists in WD."""
    check50.exists("mario-1.c")

@check50.check(exists_mario_1)
def compiles_mario_1():
    """mario-1.c compiles."""
    check50.c.compile("mario-1.c", lcs50=True)

@check50.check(compiles_mario_1)
def output_mario_1():
    """Input Number is between 0 and 100 inclusively"""
    check50.run("./mario-1").stdin("50").stdout("The input Number is: 50\n")

#Mario-2:

@check50.check()
def exists_mario_2():
    """mario-2.c exists in WD."""
    check50.exists("mario-2.c")

@check50.check(exists_mario_2)
def compiles_mario_2():
    """mario-2.c compiles."""
    check50.c.compile("mario-2.c", lcs50=True)


