class Graph(dict):
    def __init__(self):
        super().__init__()

    def add_vertex(self, key):
        self[key] = []

    def add_edge(self, origin, target, weight):
        def take_second(tup):
            return tup[1]

        if origin not in self:
            self[origin] = []

        self[origin].append((target, weight))
        if target not in self:
            self.add_vertex(target)
        self[target].append((origin, weight))
        self[origin].sort(key=take_second)
        self[target].sort(key=take_second)

    def dfs(self, start, vertex_list=[]):
        if start is None:
            return vertex_list
        if start not in vertex_list:
            vertex_list.append(start)
        else:
            return vertex_list
        for successor, weight in self[start]:
            self.dfs(successor, vertex_list)
        return vertex_list

    def bfs(self, start):
        queue = []
        vertex_list = []
        queue.append(start)
        while len(queue) != 0:
            for successor, weight in self[queue[0]]:
                if successor not in queue and successor not in vertex_list:
                    queue.append(successor)
            vertex_list.append(queue.pop(0))
        return vertex_list

    def dijkstra(self, start, end):
        graph = self
        shortest_distance = {}
        predecessor = {}
        unseenNodes = list(self.keys())
        infinity = 999999
        path = []
        for node in unseenNodes:
            shortest_distance[node] = infinity
        shortest_distance[start] = 0

        while unseenNodes:
            minNode = None
            for node in unseenNodes:
                if minNode is None:
                    minNode = node
                elif shortest_distance[node] < shortest_distance[minNode]:
                    minNode = node
            for childNode, weight in graph[minNode]:
                if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                    shortest_distance[childNode] = weight + shortest_distance[minNode]
                    predecessor[childNode] = minNode
            unseenNodes.remove(minNode)

        currentNode = end
        while currentNode != start:
            try:
                path.insert(0, currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print('Path not reachable')
                break
        path.insert(0, start)
        if shortest_distance[end] != infinity:
            return shortest_distance[end], path
