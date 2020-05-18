import check50
import check50.c

@check50.check()
def exists():
    """copycat.c exists."""
    check50.include("myletter.txt")
    check50.include("hopwarts.txt")
    check50.exists("wizardry.c")

@check50.check(exists)
def compiles():
    """copycat.c compiles."""
    check50.c.compile("wizardry.c", lcs50=True)

@check50.check(compiles)
def argc():
    """takes three command arguments"""
    check50.run("./wizardry hopwarts").stdout("./wizardry infile outfile name")
    check50.run("./wizardry").stdout("./wizardry infile outfile name")
    check50.run("./wizardry hopwarts myletter").stdout("./wizardry infile outfile name")
    check50.run("./wizardry hopwarts myletter Name1 Name2").stdout("./wizardry infile outfile name")

@check50.check(argc)
def matches():
    """You created your own letter of Acceptance"""
    check50.run("./wizardry hopwarts.txt myletter.txt Goehl")
    with open("hopwarts.txt") as file1, open("myletter.txt") as file2:
        for line1, line2 in zip(file1, file2):
            if line1 != line2:
                raise check50.Failure("texts do not match")

