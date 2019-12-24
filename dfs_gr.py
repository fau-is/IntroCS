from collections import defaultdict

class Graph(object):

    # sth is an adjacency list in the form [node, directed_edge]
    def __init__(self, sth):
        if sth is not None:
            self.sth = sth
        self.adj = defaultdict(list)
        for idx, elem in enumerate(sth):
            for i in elem:
                self.adj[idx].append(i)

    def add(self, start, end):
        self.adj[start].append(end)

    def dfs(self, root, tofind):
        nbr, path, found = self.dfs_helper(root, tofind)
        if found:
            return nbr, path
        else:
            return -1, []

    def dfs_helper(self, root, tofind):
        print(self.adj)
        stack = []
        number = 0
        path = []
        stack.insert(0, root)
        found = False
        while stack:
            cur = stack.pop(0)
            path.append(cur)
            if cur == tofind:
                found = True
                break
            number = number + 1
            for child in self.adj[cur]:
                if child not in path:
                    stack.insert(0, child)

        return number, path, found

if __name__ == "__main__":
    graph = Graph([[1,2,3],[3,4],[4],[4],[]])
    nbr, path = graph.dfs(0, 2)
    print(path)
