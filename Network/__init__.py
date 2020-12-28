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
    n = network.Graph
    n.add_vertex('A')
    if 'A' not in n:
        raise check50.Failure()