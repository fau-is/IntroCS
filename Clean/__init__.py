import check50
import check50.py

@check50.check()
def exists():
    """clean.py"""
    check50.include("silent_sea.txt")
    check50.include("silent_sea_clean.txt")
    check50.exists("clean.py")

@check50.check(exists)
def compiles():
    """clean.py runs"""
    check50.run("python3 clean.py")

@check50.check(compiles)
def matches():
    """Poem is cleaned"""
    check50.run("python3 clean.py")
    with open("silent_sea_clean.txt") as file1, open("sol.txt") as file2:
        for line1, line2 in zip(file1, file2):
            if line1 != line2:
                raise check50.Failure("Poems do not match")
