import sys

import check50
import check50.py

check50.include("network.py")

small_v = ['A', 'B', 'C', 'D']
small_e = ['AB2', 'AC3', 'BD2', 'CB4']

large_v = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
large_e = ['AB2', 'AC3', 'BD2', 'CB4', 'BE2', 'EF1', 'EG5', 'FG2']

@check50.check()
def exists():
    """network.py exists"""
    check50.exists("network.py")


@check50.check(exists)
def compiles():
    """network.py has no syntax errors"""
    check50.py.compile("network.py")


def import_network():
    network = check50.py.import_("network.py")
    if network is None:
        raise check50.Failure("import failed")
    return network


@check50.check(compiles)
def add_vertex():
    """adds vertex"""
    network = import_network()
    g = network.Graph()
    g.add_vertex('A')
    if 'A' not in g:
        raise check50.Failure("Added Vertex does not exist")


@check50.check(add_vertex)
def add_edge():
    """adds weighted edges"""
    network = import_network()

    n = network.Graph()
    for vertex in small_v:
        n.add_vertex(vertex)
    for edge in small_e:
        n.add_edge(edge[:1], edge[1], int(edge[2:]))

    # large_e outgoing A
    if ('B', 2) not in n['A'] and ('C', 3) not in n['A']:
        raise check50.Failure("large_e A->B w:2 and A->C w:3 (in requested format)", n['A'])
    # large_e outgoing B
    if ('A', 2) not in n['B'] and ('D', 2) not in n['B'] and ('C', 4) not in n['B']:
        raise check50.Failure("large_e B->A w:2; B->D w:2 and B->C w:4 (in requested format)", n['B'])
    # large_e outgoing C
    if ('A', 3) not in n['C'] and ('B', 4) not in n['C']:
        raise check50.Failure("large_e C->A w:3 and C->B w:4 (in requested format)", n['C'])
    # large_e outgoing D
    if ('B', 2) not in n['D']:
        raise check50.Mismatch("Edge D->B w:2 (in requested format)", n['D'])

@check50.check(add_edge)
def dfs():
    """performs pre-order search correctly"""
    network = import_network()

    n = network.Graph()
    for vertex in large_v:
        n.add_vertex(vertex)
    for edge in large_e:
        n.add_edge(edge[:1], edge[1], int(edge[2:]))

    #A = ['A', 'E', 'D', 'B', 'F', 'C']
    #    if A != n.dfs('A'):
    #        raise check50.Mismatch(A, n.dfs('A'))

    try:
        N = n.dfs('A')
        if N != ['A', 'E', 'D', 'B', 'F', 'C']:
            raise check50.Mismatch(A, n.dfs('A'))
    except:
        raise check50.Failure("Could not run DFS")


    #B = ['A', 'E', 'D', 'B', 'F', 'C']
    #if B != n.dfs('B'):
        #raise check50.Mismatch(A, n.dfs('B'))


@check50.check(add_edge)
def bfs():
    """performs BFS search correctly"""
    network = import_network()

    n = network.Graph()
    for vertex in large_v:
        n.add_vertex(vertex)
    for edge in large_e:
        n.add_edge(edge[:1], edge[1], int(edge[2:]))

    A = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    if A != n.bfs('A'):
        raise check50.Mismatch(A, n.bfs('A'))

    B = ['F', 'E', 'G', 'B', 'A', 'D', 'C']
    if B != n.bfs('F'):
        raise check50.Mismatch(A, n.bfs('F'))


@check50.check(add_edge)
def dijkstra():
    """performs Dijkstra correctly"""
    network = import_network()

    n = network.Graph()
    for vertex in large_v:
        n.add_vertex(vertex)
    for edge in large_e:
        n.add_edge(edge[:1], edge[1], int(edge[2:]))
    try:
        distance, path = n.dijkstra('A', 'F')
        if distance != 5 and path != ['A', 'B', 'E', 'F']:
            raise check50.Mismatch("5; ['A', 'B', 'E', 'F']", str(distance) + " " + str(path))

        distance, path = n.dijkstra('G', 'C')
        if distance != 9 and path != ['G', 'F', 'E', 'B', 'C']:
            raise check50.Mismatch("9; ['G', 'F', 'E', 'B', 'C']", str(distance) + " " + str(path))
    except:
        raise check50.Failure("Could not run Dijkstra")

