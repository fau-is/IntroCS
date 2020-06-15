import check50
import check50.c

@check50.check()
def exists():
    """clean.py"""
    check50.include("silent_sea.txt")
    check50.include("silent_sea_clean.txt")
    check50.exists("clean.py")

@check50.check(exists)
def compiles():
    """clean.py compiles"""
    check50.c.compile("clean.py", lcs50=True)

@check50.check(argc)
def matches():
    """Poem is cleaned"""
    check50.run("python clean.py")
    with open("silent_sea_clean.txt") as file1, open("sol.txt") as file2:
        for line1, line2 in zip(file1, file2):
            if line1 != line2:
                raise check50.Failure("Poems do not match")
