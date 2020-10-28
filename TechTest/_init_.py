import check50
import check50.c

#Welcome:

@check50.check()
def exists_welcome():
    """welcome.c exists in WD."""
    check50.exists("welcome.c")

@check50.check(exists_welcome)
def compiles_welcome():
    """welcome.c compiles."""
    check50.c.compile("welcome.c", lcs50=True)

@check50.check(compiles_welcome)
def output_welcome():
    """Output is correct"""
    check50.run("./welcome").stdout("Welcome to Introduction to Computer Science\n")

@check50.check(compiles_welcome)
def output_wrong():
    """This Check is only there to show you things might not always work ;)"""
    check50.run("./welcome").stdout("This is the wrong output\n")