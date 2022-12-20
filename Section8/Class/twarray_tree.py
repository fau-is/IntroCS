from graphviz import Graph

def print_array_as_bt(arr):
    g = Graph()
    g.attr('node', fillcolor='white', fontcolor='black', shape='circle', style='filled', border='black')

    for i in range(len(arr)):
        g.node(str(i), str(arr[0]))

    for i in range(len(arr)):
        if arr[i][1] != -1:
            g.edge(str(arr[i]), str(arr[i][1]))
        if arr[i][2] != -1:
            g.edge(str(arr[i]), str(arr[i][2]))

    g.render(filename="btw", format="png")

if __name__ == "__main__":
    arr = [["a", 1, 2], ["b", 3, -1], ["c", 4, 5], ["d", -1, -1], ["e", -1, -1], ["f", -1, -1]]

    print_array_as_bt(arr)