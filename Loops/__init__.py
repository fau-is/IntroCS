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
