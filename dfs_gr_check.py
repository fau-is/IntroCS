import sys
from dfs_gr import Graph


def main():
    graph = Graph([[1,2,3],[3,4],[4],[4],[]])
    nbr, path = graph.dfs(0, 2)
    return path
