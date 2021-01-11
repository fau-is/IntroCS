import check50
import check50.internal
import check50.py

check50.include('routing_tree.py')


domains1 = [("computer.com", '0.0.0.0'), ("array.com", '1.0.0.0'), ("binary.com", '0.1.0.0'),
            ("ecommerce.com", '0.0.1.0'), ("data.com", '0.0.0.1')]
domains2 = [("computer.com", '0.0.0.0'), ("array.com", '1.0.0.0'), ("binary.com", '0.1.0.0'),
            ('hardware.com', '2.0.0.0'), ("ecommerce.com", '0.0.1.0'), ('gigabyte.com', '1.1.1.1'),
            ("data.com", '0.0.0.1'), ('interconnectivity.com', '0.2.0.0')]


@check50.check()
def exists():
    """routing_tree.py exists"""
    check50.exists("routing_tree.py")


@check50.check(exists)
def compiles():
    """Routing_tree.py has no syntax errors"""
    check50.py.compile("routing_tree.py")


def imports():
    """Routing_tree.py can be imported"""
    tmp = check50.py.import_("routing_tree.py")
    if tmp is None or not hasattr(tmp, 'BST'):
        raise check50.Failure("Could not import properly")
    return tmp

@check50.check(compiles)
def add_root():
    """BST can add a single domain"""
    routing_tree = imports()
    routing_tree.BST.add('Fantastic.com', '1.1.1.1')

    if routing_tree.BST.root is None:
        raise check50.Failure("Root was None")

    if routing_tree.BST.root.domain!= 'Fantastic.com':
        raise check50.Mismatch('Fantastic.com', routing_tree.BST.root.domain)

    if routing_tree.BST.root.IP != '1.1.1.1':
        raise check50.Mismatch('1.1.1.1', routing_tree.BST.root.IP)


@check50.check(compiles)
def add_tree_child():
    """BST can add several domains"""
    routing_tree = check50.internal.import_file('routing_tree', 'routing_tree.py')
    # Build Tree
    for domain, ip in domains1:
        routing_tree.BST.add(domain, ip)
    # Root shortcut
    n = routing_tree.BST.root

    # Check root
    if n is None:
        raise check50.Failure("Root was None")
    if n.domain != 'computer.com':
        raise check50.Mismatch('sebastian.com', n.domain)
    if n.IP != '0.0.0.0':
        raise check50.Mismatch('0.0.0.0', n.IP)

    # Check left child of root
    if n.left is None:
        raise check50.Failure("Left child of root was none")
    if n.left.domain != 'array.com':
        raise check50.Mismatch('array.com', n.left.domain)
    if n.left.IP != '1.0.0.0':
        raise check50.Mismatch('1.0.0.0', n.left.IP)

    # Check right child of root
    if n.right is None:
        raise check50.Failure("Right child of root was None")
    if n.right.domain != 'ecommerce.com':
        raise check50.Mismatch('ecommerce.com', n.right.domain)
    if n.right.IP != '0.0.1.0':
        raise check50.Mismatch('0.0.1.0', n.right.IP)

    # Check root -> right -> left
    if n.right.left is None:
        raise check50.Failure('Child at root -> right -> left was None')
    if n.right.left.domain != 'data.com':
        raise check50.Mismatch('data.com', n.right.left.domain)
    if n.right.left.IP != '0.0.0.1':
        raise check50.Mismatch('0.0.0.1', n.right.left.IP)


@check50.check(add_tree_child)
def find_node():
    """BST can locate a domain and a BST node stores the correct IP address"""
    routing_tree = check50.internal.import_file('routing_tree', 'routing_tree.py')
    for domain, ip in domains1:
        routing_tree.BST.add(domain, ip)

    if routing_tree.BST.find("binary.com"):
        n = routing_tree.BST.find("binary.com")
        if n.domain != "binary.com":
            raise check50.Mismatch("binary.com", n.domain, "Find located the wrong vertex")
        if n.IP != "0.1.0.0":
            raise check50.Mismatch("0.1.0.0", n.ip, "It seems that the IP-Address is not stored correctly")
    else:
        raise check50.Failure("Could not locate a domain which should exist")


@check50.check(find_node)
def find_non_existent_node():
    """returns false if node not in tree"""
    routing_tree = check50.internal.import_file('routing_tree', 'routing_tree.py')
    for domain, ip in domains1:
        routing_tree.BST.add(domain, ip)

    if routing_tree.BST.find("nonsense.com") is not False:
        raise check50.Failure("Expected False")


@check50.check(add_tree_child)
def check_bfs():
    """Checks whether output is generated in BFS manner"""
    routing_tree = check50.internal.import_file('routing_tree', 'routing_tree.py')
    bfs = ['computer.com', 'array.com', 'hardware.com', 'binary.com', 'ecommerce.com', 'interconnectivity.com',
           'data.com', 'gigabyte.com']
    for domain, ip in domains2:
        routing_tree.BST.add(domain, ip)

    if routing_tree.BST.bfs() != bfs:
        raise check50.Mismatch(bfs, routing_tree.BST.bfs())


@check50.check(add_tree_child)
def preorder_dfs():
    """Checks whether output is in preorder-order using DFS"""
    routing_tree = check50.internal.import_file('routing_tree', 'routing_tree.py')
    dfs = ['computer.com', 'array.com', 'binary.com', 'hardware.com', 'ecommerce.com', 'data.com', 'gigabyte.com',
           'interconnectivity.com']
    for domain, ip in domains2:
        routing_tree.BST.add(domain, ip)

    if routing_tree.BST.preorder() != dfs:
        raise check50.Mismatch(dfs, routing_tree.BST.preorder())


@check50.check(find_node)
def delete():
    """Deletes Node"""
    routing_tree = check50.internal.import_file('routing_tree', 'routing_tree.py')
    for domain, ip in domains2:
        routing_tree.BST.add(domain, ip)
    n = routing_tree.BST.root
    if n is None:
        raise check50.Failure("No Root")

    # 1. Case one child
    routing_tree.BST.delete_method("array.com")
    if routing_tree.BST.find("array.com") is not False:
        raise check50.Failure("Expected deletion of array.com with one child did not occur")
    if routing_tree.BST.root.left.domain == 'array.com':
        raise check50.Failure("Deletion unsuccessful")

    # 2. Case no children
    routing_tree.BST.delete_method("data.com")
    if routing_tree.BST.find("data.com") is not False:
        raise check50.Failure("Expected deletion of data.com with no children did not occur")
    if routing_tree.BST.root.right.left.left is not None:
        raise check50.Failure("Deletion unsuccessful")

    # 3. Case two children
    routing_tree.BST.delete_method("hardware.com")
    if routing_tree.BST.find("hardware.com") is not False:
        raise check50.Failure("Expected deletion of data.com with no children did not occur")
    if routing_tree.BST.root.right.domain == 'hardware.com':
        raise check50.Failure("Deletion unsuccessful")

    # 4. Case deletes Root
    routing_tree.BST.delete_method(routing_tree.BST.root.domain)
    if routing_tree.BST.root.domain == "computer.com":
        raise check50.Failure("Root Deletion unsuccessful")
