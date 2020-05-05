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
def anagram_me():
    """Anagram me"""
    check50.run("./lowupper").stdin("mary", "army").stdout("Strings are anagrams").run("./lowupper").stdin("mary", "arny").stdout("Strings are not anagrams")
