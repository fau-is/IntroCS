import check50
import check50.c


@check50.check()
def exists_anagrams():
    """anagrams.c exists in WD."""
    check50.exists("anagrams.c")


@check50.check(exists_anagrams)
def compiles_anagrams():
    """anagrams.c compiles."""
    check50.c.compile("anagrams.c", lcs50=True)


@check50.check(compiles_anagrams)
def anagram_true():
    """It's an anagram"""
    check50.run("./anagrams").stdin("mary").stdin("army").stdout("Strings are anagrams?\n", regex=True)


@check50.check(compiles_anagrams)
def anagram_true_caseInsensitive():
    """It's a case insensitive anagram"""
    check50.run("./anagrams").stdin("mary").stdin("ARMY").stdout("Strings are anagrams?\n", regex=True)


@check50.check(compiles_anagrams)
def anagram_false():
    """Not an anagram"""
    check50.run("./anagrams").stdin("mary").stdin("arny").stdout("Strings are not anagrams?\n", regex=True)
