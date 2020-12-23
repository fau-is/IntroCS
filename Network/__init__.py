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
def add_root():
    """adds a root"""
    routing_tree.BST.add('Fantastic.com', '1.1.1.1')
    n = routing_tree.BST.root
    if n.domain != 'Fantastic.com':
        raise check50.Mismatch('Fantastic.com', n.domain)

    if n.IP != '1.1.1.1':
        raise check50.Mismatch('1.1.1.1', n.IP)