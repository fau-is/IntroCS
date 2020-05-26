import check50
import check50.c

@check50.check()
def exists():
    """linked_list.c exists."""
    check50.exists("linked_list.c")

@check50.check(exists)
def compiles():
    """linked_list.c compiles."""
    check50.c.compile("linked_list.c", lcs50=True)

@check50.check(compiles)
def check():
    """linked_list prints successfully"""
    check50.run("./linked_list").stdout("Payload 1 = 3").stdout("Payload 2 = 200").stdout("Payload 3 = 30").stdout("Payload 4 = 20").stdout("Payload 5 = 49").stdout("Payload 6 = 34").stdout("Payload 7 = 60").stdout("Payload 8 = 1").stdout("Payload 9 = 9").stdout("Payload 10 = 10")
