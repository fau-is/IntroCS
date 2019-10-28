import check50
import check50.c


@check50.check()
def compiles():
    """babylon.c compiles."""
    check50.c.compile("babylon.c", lcs50=True)


@check50.check(compiles)
def finds_2():
    """Finds that 2 is sqrt[2](4)"""
    check50.run("./babylon 2 4").stdout("2.00000").exit(0)


@check50.check(compiles)
def regards_pre_req():
    """Does not ignore the prerequisites"""
    check50.run("./babylon -2 4").stdout("Try again...").exit(-1)
    check50.run("./babylon 2 -4").stdout("Try again...").exit(-1)
    check50.run("./babylon 3 -4").stdout("-1.58741").exit(0)


@check50.check(compiles)
def finds_88_22():
    """Finds 4 in the array"""
    check50.run("./babylon 88 22").stdout("1.04616").exit(0)


@check50.check(compiles)
def finds_22_88():
    """Finds 7 in the array"""
    check50.run("./babylon 22 88").stdout("1.22573").exit(0)


@check50.check(compiles)
def finds_69_42():
    """Test not found message with 3"""
    check50.run("./linear 3").stdout("1.10709").exit(0)


@check50.check(compiles)
def usage():
    """Check usage message"""
    check50.run("./babylon").stdout("Usage: ./babylon k a").exit(1)
