import check50
import check50.py

#check50 fau-is/IntroCS/PyGraphsTrees/Network --local

check50.include('network.py')
network = check50.py.import_('network.py')

@check50.check()
def exists():
    """network.py exists"""
    check50.exists("network.py")

@check50.check(exists)
def add_vertex():
    """adds vertex"""
    n = network.Graph()
    n.add_vertex('A')
    if 'A' not in n:
        raise check50.Failure("Expected add Vertex")

@check50.check(add_vertex)
def add_edge():
    """adds weighted edges"""
    Vertices = ['A', 'B', 'C', 'D']
    Edges = ['AB2', 'AC3', 'BD2', 'CB4']
    n = network.Graph()
    for vertex in Vertices:
        n.add_vertex(vertex)
    for edge in Edges:
        n.add_edge(edge[:1], edge[1], int(edge[2:]))

    #Edges outgoing A
    if ('B', 2) not in n['A'] and ('C', 3) not in n['A']:
        raise check50.Failure("Edges A->B w:2 and A->C w:3 (in requested format)", n['A'])
    #Edges outgoing B
    if ('A', 2) not in n['B'] and ('D', 2) not in n['B'] and ('C', 4) not in n['B']:
        raise check50.Failure("Edges B->A w:2; B->D w:2 and B->C w:4 (in requested format)", n['B'])
    #Edges outgoing C
    if ('A', 3) not in n['C'] and ('B', 4) not in n['C']:
        raise check50.Failure("Edges C->A w:3 and C->B w:4 (in requested format)", n['C'])
    #Edges outgoing D
    if ('B', 2) not in n['D']:
        raise check50.Mismatch("Edge D->B w:2 (in requested format)", n['D'])

@check50.check(add_edge)
def dfs():
    """performs pre-order search correctly"""
    Vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    Edges = ['AB2', 'AC3', 'BD2', 'CB4', 'BE2', 'EF1', 'EG5', 'FG2']
    n = network.Graph()
    for vertex in Vertices:
        n.add_vertex(vertex)
    for edge in Edges:
        n.add_edge(edge[:1], edge[1], int(edge[2:]))

    A = ['A', 'E', 'D', 'B', 'F', 'C']
    if A != n.dfs('A'):
        raise check50.Mismatch(A, n.dfs('A'))

    B = ['A', 'E', 'D', 'B', 'F', 'C']
    if B != n.dfs('B'):
        raise check50.Mismatch(A, n.dfs('B'))

@check50.check(add_edge)
def bfs():
    """performs BFS search correctly"""
    Vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    Edges = ['AB2', 'AC3', 'BD2', 'CB4', 'BE2', 'EF1', 'EG5', 'FG2']
    n = network.Graph()
    for vertex in Vertices:
        n.add_vertex(vertex)
    for edge in Edges:
        n.add_edge(edge[:1], edge[1], int(edge[2:]))

    A = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    if A != n.bfs('A'):
        raise check50.Mismatch(A, n.bfs('A'))

    F = ['F', 'E', 'G', 'B', 'A', 'D', 'C']
    if B != n.bfs('F'):
        raise check50.Mismatch(A, n.bfs('F'))

@check50.check(add_edge)
def dijkstra():
    """performs Dijkstra correctly"""
    Vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    Edges = ['AB2', 'AC3', 'BD2', 'CB4', 'BE2', 'EF1', 'EG5', 'FG2']
    n = network.Graph()
    for vertex in Vertices:
        n.add_vertex(vertex)
    for edge in Edges:
        n.add_edge(edge[:1], edge[1], int(edge[2:]))

    distance, path = n.djikstra('A', 'F')
    if distance != 5 and path != ['A', 'B', 'E', 'F']:
        raise check50.Mismatch("5; ['A', 'B', 'E', 'F']", str(distance) + " " + str(path))

    distance, path = n.djikstra('G', 'C')
    if distance != 9 and path != ['G', 'F', 'E', 'B', 'C']:
        raise check50.Mismatch("9; ['G', 'F', 'E', 'B', 'C']", str(distance) + " " + str(path))






