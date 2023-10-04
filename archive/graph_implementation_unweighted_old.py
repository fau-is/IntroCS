import itertools
import graphviz
import os

def print_graph(g):
    graph = graphviz.Graph(format='png', strict=True, filename='network')
    for n in g.keys():
        graph.node(n, n)

    for n in g.keys():
        for t in g[n]:
            graph.edge(n, t)
    graph.render()
    os.remove('network')

class Graph(dict):
    def __init__(self):
        super().__init__()
        self.sps = None

    def add_vertex(self, key):
        self[key] = []

    def add_edge(self, origin, target):
        if origin not in self.keys():
            self.add_vertex(origin)
        if target not in self[origin]:
            self[origin].append(target)

        if target not in self.keys():
            self.add_vertex(target)
        if origin not in self[target]:
            self[target].append(origin)

    def remove_edge(self,edge):
        v1, v2 = edge
        index = 0
        while self[v1][index] != v2:
            index+=1
        del self[v1][index]

        index = 0
        while self[v2][index] != v1:
            index+=1
        del self[v2][index]

    # # Iterative
    def dfs(self, start):
        vertex_list = []
        stack = [start]
        visited = []
        while stack:
            node = stack.pop()
            # Important to check if node not already in vertex_list bc stack might
            # keep duplicate addresses, that have not been visited yet
            if node in vertex_list:
                continue
            visited.append(node)
            vertex_list.append(node)
            for neighbor in self[node][::-1]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return vertex_list

    # Recursive
    # def dfs(self, start, vertex_list=[]):

    #     if start in vertex_list:
    #         return
    #     vertex_list.append(start)
    #     for neighbor in self[start]:
    #         self.dfs(neighbor, vertex_list)
    #     return vertex_list

    # # Iterative
    def bfs(self, start):
        vertex_list = []
        queue = [start]
        visited = []
        while queue:
            node = queue.pop(0)
            # Important to check if node not already in vertex_list bc queue might
            # keep duplicate addresses, that have not been visited yet
            if node in vertex_list:
                continue
            vertex_list.append(node)
            visited.append(node)
            for neighbor in self[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return vertex_list

    # Recursive
    # def bfs(self, start):
    #     self.vertex_list = []
    #     queue = [start]
    #     self.bfs_helper(queue)
    #     return self.vertex_list

    # def bfs_helper(self, queue):
    #     if not queue:
    #         return
    #     node = queue.pop(0)
    #     self.vertex_list.append(node)
    #     for neighbor in self[node]:
    #         # Make sure nodes are not already in queue or vertex list
    #         if neighbor not in queue and neighbor not in self.vertex_list:
    #             queue.append(neighbor)
    #     self.bfs_helper(queue)

    def dijkstra(self, start, end):

        CurNode = (start, 0)
        queue = []
        queue_names = []
        visited = {}
        while CurNode[0] != end:
            for child in self[CurNode[0]]:
                node = child[0]
                distance = child[1] + CurNode[1]

                if node in visited.keys():
                    continue
                elif node not in queue_names:
                    idx = 0
                    for i in queue:
                        if i[1] <= distance:
                            idx += 1
                    queue.insert(idx, (node, distance, CurNode[0]))
                    queue_names.insert(idx, node)
                else:
                    idx = queue_names.index(node)
                    if distance < queue[idx][1]:
                        queue[idx] = (node, distance, CurNode[0])
            visited[CurNode[0]] = CurNode
            if queue:
                CurNode = queue.pop(0)
                queue_names.pop(0)
            else:
                return None
        visited[CurNode[0]] = CurNode

        path = []
        h = CurNode

        while h[0] != start:
            path.insert(0, h[0])
            h = visited[h[2]]

        return((CurNode[1], path))

    def most_influential_1(self):
        max_node = ''
        max_count = 0
        for node in self.keys():
            edges = len(self[node])
            if edges > max_count:
                max_count = edges
                max_node = node
        print(f"3.1 Based on the number of edges {max_node} is the most influential user with {max_count} edges.")

    def most_influential_2(self):
        mapping = {key:i for key,i in zip(self.keys(),range(len(self.keys())))}
        matrix = [[None for i in range(len(mapping))] for i in range(len(mapping))]

        for node in self.keys():
            for to_node in self.keys():
                if node == to_node:
                    continue
                # matrix[mapping[node]][mapping[to_node]] = self.dijkstra(node,to_node)
                matrix[mapping[node]][mapping[to_node]] = self.bfs_find(node, to_node)

        ranking = {node:0 for node in self.keys()}
        for row in matrix:
            for i in row:
                if i:
                   path = i
                   # path = i[1]
                   for node in path:
                       ranking[node] += 1
        max_node = max(ranking, key=ranking.get)
        max_value = ranking[max_node]
        print(f"3.2 BFS/Dijkstra - Based on 'Betweenness' the most influential user is {max_node} as it belongs to {max_value} shortest paths.")

    def most_influential_3(self):
        mapping = {key:i for key,i in zip(self.keys(),range(len(self.keys())))}
        mapping_rev = {i:key for key, i in mapping.items()}
        matrix = [[None for i in range(len(mapping))] for i in range(len(mapping))]

        for node in self.keys():
            for to_node in self.keys():
                if node == to_node:
                    continue
                matrix[mapping[node]][mapping[to_node]] = self.bfs_find(node,to_node)
                # matrix[mapping[node]][mapping[to_node]] = self.dijkstra(node, to_node)

        sps = {node:[] for node in self.keys()}
        for y,row in enumerate(matrix):
            for i in row:
                if i:
                   length = len(i)
                   # length = i[0]
                   sps[mapping_rev[y]].append(length)
        ranking = {key: sum(value)/len(value) for key, value in sps.items()}
        min_node = min(ranking, key=ranking.get)
        min_mean_distance = ranking[min_node]
        print(f"3.3 BFS/Dijkstra - Based on 'Closeness' the most influential user is {min_node} as it has on avarage the closest distance of {min_mean_distance} to other nodes.")

    def most_popular(self, included=None):
        if included:
            return (included,) + max(self[included], key=lambda x: x[1])
        else:
            max_per_key = {key:max(self[key], key=lambda x: x[1]) for key in self.keys()}
            return max([(key,) + value for key,value in max_per_key.items()], key= lambda x: x[2])
    def most_versatile(self):
        comb_no = {key:len(value) for key, value in self.items()}
        return (max(comb_no, key=comb_no.get),max(comb_no.values()))

    def bfs_find(self, start, end):
        queue = [(start, [start])]
        visited = set()

        while queue:
            (node, path) = queue.pop(0)
            if node not in visited:
                if node == end:
                    return path
                visited.add(node)

                for neighbor in self[node]:
                    queue.append((neighbor, path + [neighbor]))

        return None

    def edge_in_sp(self, pair, sp):
        if sp == None:
            return False
        elif len(sp) <2:
            return False
        pairs = [(sp[i],sp[i+1]) for i in range(len(sp)-1)]
        if pair in pairs:
            return True
        elif (pair[1],pair[0]) in pairs:
            return True
        else:
            return False

    def compute_sps(self):
        # Mapping keys to indexes i=0,1,...,len(keys())-1
        mapping = {key: i for key, i in zip(self.keys(), range(len(self.keys())))}
        # Reverse mapping
        mapping_rev = {i: key for key, i in mapping.items()}
        # Creation of nxn Matrix while n=number of nodes
        matrix = [[None for i in range(len(mapping))] for i in range(len(mapping))]
        for i in range(len(matrix)):
            for y in range(len(matrix)):
                # populating the sps matrix with shortest paths between all pairs of nodes
                matrix[i][y] = self.bfs_find(mapping_rev[i], mapping_rev[y])
        # gets updated after each edge deletion
        self.sps = matrix

    def connected_component_subgraphs(self):
        subs = []
        to_visit = set(self.keys())
        while to_visit:
            # complete subgraph identified via dfs
            connected = set(self.dfs(list(to_visit)[0]))
            subs.append(connected)
            # all nodes part of the subgraphs are removed from the list "to_visit"
            to_visit -= connected
        return subs

    def edge_to_remove(self):
        # list of all possible pairs = edges
        pairs = list(itertools.combinations(self.keys(), 2))
        # initializing betweeness metric with 0 for each edge
        edge_betweenness = {pair:0 for pair in pairs}
        # number of all possible edges
        all_edges = len(self.keys())*(len(self.keys())-1)
        for pair in pairs:
            abs = 0
            # iteration over every existing shortest path
            for i in range(len(self.sps)):
                for y in range(len(self.sps)):
                    if i == y:
                        continue
                    if self.edge_in_sp(pair, self.sps[i][y]):
                        abs +=1
            # egde_betweeness = # sps with current edge / # all edges
            edge_betweenness[pair] += abs/all_edges
        list_of_tuples = list(edge_betweenness.items())
        # sorting based on edge_betweeness
        list_of_tuples.sort(key= lambda x: -x[1])
        return list_of_tuples[0][0]


    def get_communities(self, clusters):
        # 1. get disconnected subgraphs
        c = self.connected_component_subgraphs()
        while len(c) < clusters:
            # 2. Compute shortest paths (via BFS/Dijkstra) between every pair of nodes
            self.compute_sps()
            # 3. The Betweenness of all existing edges in the network is calculated, edge with the highest Betweenness returned.
            edge_to_remove = self.edge_to_remove()
            # 4. The edge is removed.
            self.remove_edge(edge_to_remove)
            # 1. get disconnected subgraphs
            c = self.connected_component_subgraphs()
        return c

