from graphviz import Graph

def print_array_as_bt(arr):
    g = Graph()
    g.attr('node', fillcolor='white', fontcolor='black', shape='circle', style='filled', border='black')
    for node in arr:
        g.node(str(node), str(node))

    for i in range(len(arr)):
        if ((2 * i) + 1) < len(arr):
            g.edge(str(arr[i]), str(arr[(2 * i) + 1]))
        if ((2 * i) + 2) < len(arr):
            g.edge(str(arr[i]), str(arr[(2 * i) + 2]))

    g.render(filename="bt", format="png")


if __name__ == '__main__':
    arr = [18, 13, 35, 12, 15]

    print_array_as_bt(arr)