import check50
import check50.c

@check50.check()
def exists():
    """copycat.c exists."""
    check50.include("copy.txt")
    check50.include("original.txt")
    check50.exists("copycat.c")

@check50.check(exists)
def compiles():
    """copycat.c compiles."""
    check50.c.compile("copycat.c", lcs50=True)

@check50.check(compiles)
def first_line():
    """Text is correct"""
    check50.run("./copycat")
    with open("original.txt") as file1, open("copy.txt") as file2:
        for line1, line2 in zip(file1, file2):
            if line1 != line2:
                raise check50.Failure("texts do not match")

