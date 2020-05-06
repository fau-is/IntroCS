import check50
import check50.c


@check50.check()
def compiles():
    """strspcpy.c compiles."""
    check50.c.compile("strspcpy.c")

@check50.check(compiles)
def check_two_inputs():
    """Checks whether the program exits with code 1 if there are not exactly 2 inputs"""
    check50.run("./strspcpy").exit(1)
    check50.run("./strspcpy 10").exit(1)
    check50.run("./strspcpy 10 hello world").exit(1)

@check50.check(compiles)
def check_first_input_is_number():
    """Checks if exits with code 2 if first input is not a number"""
    check50.run("./strspcpy 10 hello").exit(0)
    check50.run("./strspcpy af hello").exit(2)
    check50.run("./strspcpy 1b hello").exit(2)


@check50.check(compiles)
def check_second_input_is_alpha():
    """Checks if exits with code 3 if non alphabetical character in second input"""
    check50.run("./strspcpy 10 stup1d").exit(3)
    check50.run("./strspcpy 10 where)").exit(3)
    check50.run("./strspcpy 10 l3v3r4g3").exit(3)


@check50.check(compiles)
def check_copy():
    """Can print 3 to 10 characters repetitively"""
    check50.run("./strspcpy 10 abc").stdout("abcabcabca\n")


@check50.check(compiles)
def check_copy_small():
    """Can copy a large string into a small output"""
    check50.run("./strspcpy 1 abc").stdout("a\n")


@check50.check(compiles)
def check_copy_same_size():
    """Can replicate the string exactly"""
    check50.run("./strspcpy 3 abc").stdout("abc\n")

