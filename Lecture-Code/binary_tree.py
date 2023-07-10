from graphviz import Graph
import sys

sys.path.append("C:\Program Files\Graphviz\bin")

if __name__ == '__main__':
    arr = [18, 13, 35, 12, 15]
    g = Graph()
    g.attr('node', fillcolor='white', fontcolor='black', shape='circle', style='filled', border='black')
    for node in arr:
        g.node(str(node), str(node))

    for i in range(len(arr)):
        if ((2 * i) + 1) < len(arr):
            g.edge(str(arr[i]), str(arr[(2 * i) + 1]))
        if ((2 * i) + 2) < len(arr):
            g.edge(str(arr[i]), str(arr[(2 * i) + 2]))

    g.view(filename="bt")