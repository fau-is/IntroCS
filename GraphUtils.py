import json


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

