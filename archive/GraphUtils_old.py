import json
import itertools


class User():
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Graph(dict):
    def __init__(self):
        super().__init__()
        self.sps = None

    def add_vertex(self, user):
        self[str(user)] = []  # Use the string representation of the user as the key

    def add_edge(self, origin, target):
        if str(origin) not in self.keys():
            self.add_vertex(origin)
        if str(target) not in self.keys():
            self.add_vertex(target)

        # Insert str(target) into origin's neighbors
        if str(target) not in self[str(origin)]:
            self[str(origin)].append(str(target))
            self[str(origin)].sort()  # sort the list in ascending order

        # Insert str(origin) into target's neighbors
        if str(origin) not in self[str(target)]:
            self[str(target)].append(str(origin))
            self[str(target)].sort()  # sort the list in ascending order


    def remove_edge(self, edge):
        v1 = str(edge[0])
        v2 = str(edge[1])
        index = 0
        while self[v1][index] != v2:
            index+=1
        del self[v1][index]
        index = 0
        while self[v2][index] != v1:
            index+=1
        del self[v2][index]

    def remove_vertex(self, user):
        for neighbors in self.values():
            if user in neighbors:
                neighbors.remove(user)
        del self[user]


    def dfs(self, start):
        vertex_list = []
        stack = [str(start)]
        visited = []
        while stack:
            node = stack.pop()
            if node in vertex_list:
                continue
            visited.append(node)
            vertex_list.append(node)
            for neighbor in self[node][::-1]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return vertex_list

    def find_clusters(self):
        visited = set()
        clusters = []

        for vertex in self:
            if vertex not in visited:
                cluster = self.dfs(vertex)
                visited.update(cluster)
                clusters.append(cluster)

        return clusters

    def bfs(self, start):
        vertex_list = []
        queue = [str(start)]
        visited = []
        while queue:
            node = queue.pop(0)
            if node in vertex_list:
                continue
            vertex_list.append(node)
            visited.append(node)
            for neighbor in self[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return vertex_list

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


    def most_influential(self):
        mapping = {key: i for key, i in zip(self.keys(), range(len(self.keys())))}
        mapping_rev = {i: key for key, i in mapping.items()}
        matrix = [[None for i in range(len(mapping))] for i in range(len(mapping))]

        for node in self.keys():
            for to_node in self.keys():
                if node == to_node:
                    continue
                matrix[mapping[node]][mapping[to_node]] = self.bfs_find(node, to_node)
                # matrix[mapping[node]][mapping[to_node]] = self.dijkstra(node, to_node)

        sps = {node: [] for node in self.keys()}
        for y, row in enumerate(matrix):
            for i in row:
                if  i:
                    length = len(i)
                    # length = i[0]
                    sps[mapping_rev[y]].append(length)
        ranking = {key: sum(value) / len(value) for key, value in sps.items() if len(value) > 0}
        min_node = min(ranking, key=ranking.get)
        min_mean_distance = ranking[min_node]
        return(min_node, min_mean_distance)

    def build_graph(self, filepath='tests/ressources/graph_52n.json'):
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Remove the first key-item pair
        first_key = list(data.keys())[0]
        del data[first_key]
        # Add vertices and edges to the graph
        for key, neighbors in data.items():
            key_user = User(key)
            self.add_vertex(key_user)
            for neighbor in neighbors:
                neighbor_user = User(neighbor)
                self.add_edge(key_user, neighbor_user)

    def edge_in_sp(self, pair, sp):
        if sp == None:
            return False
        elif len(sp) <2:
            return False
        pairs = [(sp[i],sp[i+1]) for i in range(len(sp)-1)]
        if pair in pairs:
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

    def edge_to_remove(self):
        # list of all possible pairs = edges
        pairs = list(itertools.combinations(self.keys(), 2))
        # initializing betweeness metric with 0 for each edge
        edge_betweenness = {pair:0 for pair in pairs}
        # number of all possible edges
        sps_count = len(self.keys())*(len(self.keys())-1)
        for pair in pairs:
            abs = 0
            # iteration over every existing shortest path
            for i in range(len(self.sps)):
                for y in range(len(self.sps)):
                    if i == y:
                        continue
                    if self.edge_in_sp(pair, self.sps[i][y]):
                        abs += 1
            # egde_betweeness = # sps with current edge / # all edges
            edge_betweenness[pair] = abs/sps_count
        list_of_tuples = list(edge_betweenness.items())
        # sorting based on edge_betweeness
        list_of_tuples.sort(key= lambda x: -x[1])
        return list_of_tuples[0][0]

    def get_communities(self, clusters):
        # 1. get disconnected subgraphs
        c = self.find_clusters()
        while len(c) < clusters:
            # 2. Compute shortest paths (via BFS/Dijkstra) between every pair of nodes
            self.compute_sps()
            # 3. The Betweenness of all existing edges in the Mastodon_network is calculated, edge with the highest Betweenness returned.
            edge_to_remove = self.edge_to_remove()
            # 4. The edge is removed.
            self.remove_edge(edge_to_remove)
            # 1. get disconnected subgraphs
            c = self.find_clusters()
        return c

if __name__ == "__main__":
    graph = Graph()
    graph.build_graph()
    print(graph)
    print(graph.most_influential())