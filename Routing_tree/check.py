
from routing_tree import BST as Tree

sup_tree = [("computer.com", '0.0.0.0'), ("array.com", '1.0.0.0'), ("binary.com", '0.1.0.0'),
            ('hardware.com', '2.0.0.0'),
            ("ecommerce.com", '0.0.1.0'), ('gigabyte.com', '1.1.1.1'), ("data.com", '0.0.0.1'),
            ('interconnectivity.com', '0.2.0.0')]

g = Tree
for domain, ip in sup_tree:
    g.add(domain, ip)

BFS = g.bfs()
print(BFS)
DFS = g.preorder()
print(DFS)

g.deleteBST(g.root, "array.com")
print(g.preorder())