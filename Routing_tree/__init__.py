import check50
import check50.py

#check50 fau-is/IntroCS/PyGraphsTrees/Routing_tree --local

check50.include('routing_tree.py')
routing_tree = check50.py.import_('routing_tree.py')

@check50.check()
def exists():
    """routing_tree.py exists"""
    check50.exists("routing_tree.py")


@check50.check(exists)
def add_root():
    """adds a root"""
    routing_tree.BST.add('Fantastic.com', '1.1.1.1')
    n = routing_tree.BST.root
    if n.domain != 'Fantastic.com':
        raise check50.Mismatch('Fantastic.com', n.domain)

    if n.IP != '1.1.1.1':
        raise check50.Mismatch('1.1.1.1', n.IP)


@check50.check(add_root)
def add_tree_child():
    """adds children"""
    BST = [("sebastian.com", '0.0.0.0'), ("sebastion.com", '1.0.0.0'), ("sabastian.com", '0.1.0.0'),
           ("sebastimon.com", '0.0.1.0')]
    for domain, ip in BST:
        routing_tree.BST.add(domain, ip)
    n = routing_tree.BST.root
    if n is None:
        raise check50.Failure()
    if n.domain != 'sebastian.com':
        raise check50.Mismatch('sebastian.com', n.domain)

    if n.IP != '0.0.0.0':
        raise check50.Mismatch('0.0.0.0', n.IP)

    n = n.left
    if n is None:
        raise check50.Failure()
    if n.domain != 'sabastian.com':
        raise check50.Mismatch('sabastian.com', n.domain)

    if n.IP != '0.1.0.0':
        raise check50.Mismatch('0.1.0.0', n.IP)

    n = routing_tree.BST.root.right
    if n is None:
        raise check50.Failure()

    if n.domain != 'sebastion.com':
        raise check50.Mismatch('sebastion.com', n.domain)

    if n.IP != '1.0.0.0':
        raise check50.Mismatch('1.0.0.0', n.IP)

    n = routing_tree.BST.root.right.left
    if n is None:
        raise check50.Failure()

    if n.domain != 'sebastimon.com':
        raise check50.Mismatch('sebastimon.com', n.domain)

    if n.IP != '0.0.1.0':
        raise check50.Mismatch('0.0.1.0', n.IP)


@check50.check(add_tree_child)
def find_node():
    """finds node"""
    BST = [("computer.com", '0.0.0.0'), ("array.com", '1.0.0.0'), ("binary.com", '0.1.0.0'),
           ("ecommerce.com", '0.0.1.0'), ("data.com", '0.0.0.1')]
    for domain, ip in BST:
        routing_tree.BST.add(domain, ip)

    if routing_tree.BST.find("binary.com") is None:
        raise check50.Failure("Did not expect None-type")
    if routing_tree.BST.find("binary.com") is False:
        raise check50.Failure("Did not expect bool=False")
    if routing_tree.BST.find("binary.com"):
        n = routing_tree.BST.find("binary.com")
        if n.domain != "binary.com":
            raise check50.Mismatch("binary.com", n.domain)

@check50.check(add_tree_child)
def reject_find_node():
    """returns false if node not in tree"""
    BST = [("computer.com", '0.0.0.0'), ("array.com", '1.0.0.0'), ("binary.com", '0.1.0.0'),
           ("ecommerce.com", '0.0.1.0'), ("data.com", '0.0.0.1')]
    for domain, ip in BST:
        routing_tree.BST.add(domain, ip)

    if routing_tree.BST.find("nonsense.com") is not False:
        raise check50.Failure("Expected false")
    if routing_tree.BST.find("binary.com") is False:
        raise check50.Failure("Should not return bool=False")


@check50.check(add_tree_child)
def bfs():
    """Breadth First Search is correct"""
    BFS = ['computer.com', 'array.com', 'hardware.com', 'binary.com', 'ecommerce.com', 'interconnectivity.com', 'data.com', 'gigabyte.com']
    BST = [("computer.com", '0.0.0.0'), ("array.com", '1.0.0.0'), ("binary.com", '0.1.0.0'), ('hardware.com', '2.0.0.0'),
           ("ecommerce.com", '0.0.1.0'), ('gigabyte.com', '1.1.1.1'), ("data.com", '0.0.0.1'), ('interconnectivity.com', '0.2.0.0')]

    if routing_tree.BST.bfs() != BFS:
        raise check50.Mismatch(BFS, routing_tree.BST.bfs())


@check50.check(add_tree_child)
def preorder_dfs():
    """pre-order DFS is correct"""
    DFS = ['array.com', 'binary.com', 'computer.com', 'data.com', 'ecommerce.com', 'gigabyte.com', 'hardware.com', 'interconnectivity.com']
    BST = [("computer.com", '0.0.0.0'), ("array.com", '1.0.0.0'), ("binary.com", '0.1.0.0'), ('hardware.com', '2.0.0.0'),
           ("ecommerce.com", '0.0.1.0'), ('gigabyte.com', '1.1.1.1'), ("data.com", '0.0.0.1'), ('interconnectivity.com', '0.2.0.0')]

    if routing_tree.BST.preorder() != DFS:
        raise check50.Mismatch(DFS, routing_tree.BST.preorder())