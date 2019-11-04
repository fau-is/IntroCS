import check50
import check50.c


@check50.check()
def compiles():
    """insertSort.c compiles."""
    check50.c.compile("insertSort.c", lcs50=True)

@check50.check(compiles)
def regards_pre_req():
    """Does not ignore the prerequisites"""
    check50.run("./insertSort asc some string ").stdout("Usage: ./insertSort [asc|dsc]\n").exit(1)
    check50.run("./insertSort somestring").stdout("Usage: ./insertSort [asc|dsc]\n").exit(1)
    check50.run("./insertSort").stdout("Usage: ./insertSort [asc|dsc]\n").exit(0)

@check50.check(compiles)
def sort_introcs():
    """Sorts IntroCS correctly without capital letters"""
    check50.run("./insertSort asc introcs").stdout("cinorst").exit(0)
    check50.run("./insertSort dsc introcs").stdout("tsronic").exit(0)

@check50.check(compiles)
def sort_IntroCS():
    """Finds correct root for k = 88 and a = 22"""
    check50.run("./babylon 88 22").stdout("1.04616").exit(0)


@check50.check(compiles)
def finds_22_88():
    """Sorts IntroCS alphabetically without capital letters"""
    check50.run("./insertSort asc IntroCS").stdout("CInorSt").exit(0)
    check50.run("./insertSort dsc IntroCS").stdout("tSronIC").exit(0)
