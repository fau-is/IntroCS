import check50
import check50.py

check50.include('routing_tree.py')
routing_tree = check50.py.import_('routing_tree.py')

@check50.check()
def exists():
    """routing_tree.py & dns.py exist"""
    check50.exists("routing_tree.py")


@check50.check()
def add_root():
    """adds a root"""
    routing_tree.Node.add('Fantastic.com', '1.1.1.1')
    n = routing_tree.Node.root
    if n.domain != 'Fantastic.com':
        raise check50.Mismatch('Fantastic.com', n.domain)

    if n.IP != '1.1.1.1':
        raise check50.Mismatch('1.1.1.1', n.IP)


@check50.check()
def add_tree_child():
    """adds children"""
    BST = [("sebastian.com", '0.0.0.0'), ("sebastion.com", '1.0.0.0'), ("sabastian.com", '0.1.0.0'),
           ("sebastimon.com", '0.0.1.0')]
    for domain, ip in BST:
        routing_tree.Node.add(domain, ip)
    n = routing_tree.Node.root
    if n.domain != 'sebastian.com':
        raise check50.Mismatch('sebastian.com', n.domain)

    if n.IP != '0.0.0.0':
        raise check50.Mismatch('0.0.0.0', n.IP)

    n = n.left
    if n.domain != 'sabastian.com':
        raise check50.Mismatch('sabastian.com', n.domain)

    if n.IP != '0.1.0.0':
        raise check50.Mismatch('0.1.0.0', n.IP)

    n = routing_tree.Node.root.right
    if n.domain != 'sabastion.com':
        raise check50.Mismatch('sabastion.com', n.domain)

    if n.IP != '1.0.0.0':
        raise check50.Mismatch('1.0.0.0', n.IP)

    n = routing_tree.Node.root.right.right
    if n.domain != 'sebastimon.com':
        raise check50.Mismatch('sebastimon.com', n.domain)

    if n.IP != '0.0.1.0':
        raise check50.Mismatch('0.0.1.0', n.IP)
