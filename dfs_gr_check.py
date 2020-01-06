import sys
from dfs_gr import Graph


if __name__ == '__main__':
    graph = Graph([[1,2,3],[3,4],[4],[4],[]])
    nbr, path = graph.dfs(0, 2)
    print(path, end="")
