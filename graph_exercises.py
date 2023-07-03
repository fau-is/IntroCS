class Graph(dict):
    def __init__(self):
        super().__init__()

    def add_vertex(self, key):
        self[key] = []

    def add_edge(self, origin, target, weight):
        if origin not in self.keys():
            self.add_vertex(origin)
        insert_idx = self.get_index(origin, target, weight)
        self[origin].insert(insert_idx, (target, weight))

        if target not in self.keys():
            self.add_vertex(target)
        insert_idx = self.get_index(target, origin, weight)
        self[target].insert(insert_idx, (origin, weight))

    def get_index(self, origin, target, weight):
        idx = 0
        length = len(self[origin])
        if length == 0:
            return 0
        while self[origin][idx][1] < weight:
            idx +=1
            if idx == length:
                return idx
        while self[origin][idx][1] == weight and self[origin][idx][0].lower() < target.lower():
            idx +=1
            if idx == length:
                return idx
        return idx

    # # Iterative
    def dfs(self, start, vertex_list=[]):

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
                if neighbor[0] not in visited:
                    stack.append(neighbor[0])
        return vertex_list

    # Recursive
    # def dfs(self, start, vertex_list=[]):

    #     if start in vertex_list:
    #         return
    #     vertex_list.append(start)
    #     for neighbor in self[start]:
    #         self.dfs(neighbor[0], vertex_list)
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
                if neighbor[0] not in visited:
                    queue.append(neighbor[0])
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
    #         if neighbor[0] not in queue and neighbor[0] not in self.vertex_list:
    #             queue.append(neighbor[0])
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
        print(f"Based on the number of edges {max_node} is the most influential user with {max_count} edges.")

    def most_influential_2(self):
        mapping = {key:i for key,i in zip(self.keys(),range(len(self.keys())))}
        matrix = [[None for i in range(len(mapping))] for i in range(len(mapping))]

        for node in self.keys():
            for to_node in self.keys():
                if node == to_node:
                    continue
                matrix[mapping[node]][mapping[to_node]] = self.dijkstra(node,to_node)

        ranking = {node:0 for node in self.keys()}
        for row in matrix:
            for i in row:
                if i:
                   path = i[1]
                   for node in path:
                       ranking[node] += 1
        max_node = max(ranking, key=ranking.get)
        max_value = ranking[max_node]
        print(f"Based on 'Betweenness' the most influential user is {max_node} as it belongs to {max_value} shortest paths.")

    def most_influential_3(self):
        mapping = {key:i for key,i in zip(self.keys(),range(len(self.keys())))}
        mapping_rev = {i:key for key, i in mapping.items()}
        matrix = [[None for i in range(len(mapping))] for i in range(len(mapping))]

        for node in self.keys():
            for to_node in self.keys():
                if node == to_node:
                    continue
                matrix[mapping[node]][mapping[to_node]] = self.dijkstra(node,to_node)

        sps = {node:[] for node in self.keys()}
        for y,row in enumerate(matrix):
            for i in row:
                if i:
                   length = i[0]
                   sps[mapping_rev[y]].append(length)
        ranking = {key: sum(value)/len(value) for key, value in sps.items()}
        min_node = min(ranking, key=ranking.get)
        min_mean_distance = ranking[min_node]
        print(f"Based on 'Closeness' the most influential user is {min_node} as it has on avarage the closest distance of {min_mean_distance} to other nodes.")
