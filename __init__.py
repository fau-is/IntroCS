import check50
import check50.c


@check50.check()
def compiles():
    """"runs"""
    check50.run("python qsort.py").stdout("No arguments!", regex=False).exit(0)


@check50.check(compiles)
def sorts_asc():
    """Sorts stuff"""
    check50.run("python qsort.py asldkgapqoejr").stdout("[ a, a, d, e, g, j, k, l, o, p, q, r, s ]", regex=False).exit(0)


@check50.check(compiles)
def sorts_dsc():
    """Sorts other stuff"""
    check50.run("python qsort.py 1i6u5039431ÖALKJgj1p23O9").stdout("[ 0, 1, 1, 1, 2, 3, 3, 3, 4, 5, 6, 9, 9, A, J, K, L, O, g, i, j, p, u, Ö ]", regex=False).exit(0)


@check50.check(compiles)
def usage():
    """Sorts a lot"""
    check50.run("python qsort.py alskfjqiejr123io5udbagkdsf1384rasjdf1u3").stdout("[ 1, 1, 1, 2, 3, 3, 3, 4, 5, 8, a, a, a, b, d, d, d, e, f, f, f, g, i, i, j, j, j, k, k, l, o, q, r, r, s, s, s, u, u ]", regex=False).exit(0)
