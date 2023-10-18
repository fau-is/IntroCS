from typing import List, Tuple, Optional, Union
import json
import itertools
import graphviz
import os


class User():
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Graph(dict):
    """
    A graph object based on a dictionary implementation.

    Attributes:
    ----------
    sps: n*n (2-dimensional) matrix to store shortest paths between all nodes

    Methods:
    ----------
    add_vertex()
    """
    def __init__(self) -> None:
        """
        Initialize the Graph object as an empty dictionary.
        """
        super().__init__()
        self.sps = None # Shortest path matrix, initialized as None

    def add_vertex(self, user: object) -> None:
        """
        Adds a vertex to the graph.

        Parameters:
        ----------
        user: The user object or identifier to be added as a vertex.
        """
        self[str(user)] = []  # Use the string representation of the user as the key

    def add_edge(self, origin: object, target: object) -> None:
        """
        Adds an edge to the graph between `origin` and `target`.

        Parameters:
        ----------
        origin: The originating vertex.
        target: The target vertex.
        """
        origin_str, target_str = str(origin), str(target)

        # Add vertices if they do not exist
        if origin_str not in self:
            self.add_vertex(origin)
        if target_str not in self:
            self.add_vertex(target)

        # Add the edges
        if target_str not in self[origin_str]:
            self[origin_str].append(target_str)
            self[origin_str].sort() # sort the list in ascending order

        if origin_str not in self[target_str]:
            self[target_str].append(origin_str)
            self[target_str].sort() # sort the list in ascending order


    def remove_edge(self, edge: Tuple[object, object]) -> None:
        """
        Removes an edge from the graph.

        Parameters:
        ----------
        edge: Tuple containing the vertices that form the edge.
        """
        v1, v2 = str(edge[0]), str(edge[1])

        # Remove the edge by deleting the corresponding entries
        if v2 in self[v1]:
            self[v1].remove(v2)
        if v1 in self[v2]:
            self[v2].remove(v1)

    def remove_vertex(self, user: object) -> None:
        """
        Removes a vertex and all its edges from the graph.

        Parameters:
        ----------
        user: The user object or identifier to be removed.
        """
        user_str = str(user)

        # Remove vertex from neighbors lists
        for neighbors in self.values():
            if user_str in neighbors:
                neighbors.remove(user_str)

        # Remove vertex from the graph
        if user_str in self:
            del self[user_str]


    def dfs(self, start: object) -> List[str]:
        """
        Depth-first search starting from `start` vertex.

        Parameters:
        ----------
        start: The starting vertex.

        Returns:
        ----------
        List of visited vertices.
        """
        visited = []
        stack = [str(start)]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.append(node)

            # Add unvisited neighbors to stack
            for neighbor in reversed(self[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

        return visited

    def get_subgraphs(self) -> List[List[str]]:
        """
        Finds disconnected subgraphs (clusters) in the graph.

        Returns:
        ----------
        List of subgraphs, where each subgraph is a list of vertices.
        """
        visited = set()
        subgraphs = []

        for vertex in self:
            if vertex not in visited:
                cluster = self.dfs(vertex)
                visited.update(cluster)
                subgraphs.append(cluster)

        return subgraphs

    # def bfs(self, start):
    #     vertex_list = []
    #     queue = [str(start)]
    #     visited = []
    #     while queue:
    #         node = queue.pop(0)
    #         if node in vertex_list:
    #             continue
    #         vertex_list.append(node)
    #         visited.append(node)
    #         for neighbor in self[node]:
    #             if neighbor not in visited:
    #                 queue.append(neighbor)
    #     return vertex_list

    def shortest_path(self, start: object, end: object) -> Union[List[str],None]:
        """
        Breadth-first search from `start` to `end` with path tracking to identify the shortest path.

        Parameters:
        ----------
        start: The starting vertex.
        end: The end vertex.

        Returns:
        ----------
        List of vertices forming the shortest path from start to end, or None if there is no path.
        """
        queue = [(start, [start])]
        visited = set()

        # BFS loop
        while queue:
            # Dequeue a node and path
            node, path = queue.pop(0)

            # If the node hasn't been visited yet
            if node not in visited:
                # Check if the current node is the end node
                if node == end:
                    return path

                # Mark the current node as visited
                visited.add(node)

                # Get neighbors of the current node
                neighbors = self[node]

                # Enqueue neighbors
                for neighbor in neighbors:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

        return None


    def most_influential(self) -> Tuple[str, float]:
        """
        Identifies the most influential user based on average shortest path length.

        Returns:
        ----------
        Tuple containing the most influential user and its average shortest path length.
        """
        # Create mappings from node keys to indices and vice versa
        mapping = {key: index for index, key in enumerate(self.keys())}
        mapping_rev = {index: key for key, index in mapping.items()}

        # Initialize a matrix to store shortest paths between nodes
        matrix = [[None for _ in range(len(mapping))] for _ in range(len(mapping))]

        # Populate the matrix with shortest paths between nodes
        for from_node in self.keys():
            for to_node in self.keys():
                if from_node == to_node:
                    continue

                shortest_path = self.shortest_path(from_node, to_node)
                matrix[mapping[from_node]][mapping[to_node]] = shortest_path

        # Initialize a dictionary to store the lengths of shortest paths for each node
        sps_lengths = {node: [] for node in self.keys()}

        # Populate the sps_lengths dictionary with the lengths of shortest paths
        for y, row in enumerate(matrix):
            for path in row:
                if path:
                    length = len(path)
                    sps_lengths[mapping_rev[y]].append(length)

        # Calculate the average shortest path length for each node
        sp_len_avgs = {key: sum(value) / len(value) for key, value in sps_lengths.items() if len(value) > 0 }

        # Identify the most influential node based on minimum average shortest path length
        min_node = min(sp_len_avgs, key=sp_len_avgs.get)
        min_avg_distance = sp_len_avgs[min_node]

        return min_node, min_avg_distance

    def edge_in_sp(self, pair: Tuple[str, str], sp: List[str]) -> bool:
        """
        Checks if an edge exists in the given shortest path.

        Parameters:
        ----------
        pair: Tuple containing the users that form the edge.
        sp: The shortest path, represented as a list of vertices.

        Returns:
        ----------
        Boolean value indicating the presence of the edge in the shortest path.
        """
        # Check if the shortest path exists or is too short to contain an edge
        if sp is None or len(sp) < 2:
            return False

        # Create list of edge pairs in the shortest path
        pairs_in_sp = [(sp[i], sp[i+1]) for i in range(len(sp) - 1)]

        # Check if the given edge pair is in the shortest path
        return pair in pairs_in_sp

    def compute_sps(self) -> None:
        """
        Computes shortest paths between every pair of nodes and stores them in `self.sps`.
        """
        # Create a mapping of nodes to integers
        mapping = {key: idx for idx, key in enumerate(self.keys())}
        reverse_mapping = {idx: key for key, idx in mapping.items()}

        # Initialize the shortest paths matrix
        n = len(mapping)
        self.sps = [[None] * n for _ in range(n)]

        # Populate the shortest paths matrix
        for i in range(n):
            for j in range(n):
                self.sps[i][j] = self.shortest_path(reverse_mapping[i], reverse_mapping[j])

    def edge_to_remove(self) -> Tuple[str, str]:
        """
        Identifies the edge to remove based on edge betweenness.

        Returns:
        ----------
        Tuple containing the vertices of the edge to remove.
        """
        # Generate all unique pairs of nodes (potential edges)
        pairs = list(itertools.combinations(self.keys(), 2))

        # Initialize the edge betweenness dictionary
        edge_betweenness = {pair: 0 for pair in pairs}

        # Calculate total number of possible shortest paths
        total_sps = len(self.keys()) * (len(self.keys()) - 1)

        # Calculate edge betweenness for each pair
        for pair in pairs:
            count = 0  # count of shortest paths containing this edge
            for row in self.sps:
                for sp in row:
                    if self.edge_in_sp(pair, sp):
                        count += 1
            edge_betweenness[pair] = count / total_sps

        # Sort edges by betweenness and pick the one with highest betweenness
        sorted_edges = sorted(edge_betweenness.items(), key=lambda x: -x[1])
        return sorted_edges[0][0]

    def girvan_newman_algorithm(self, clusters: int) -> List[List[str]]:
        """
        Applies the Girvan-Newman algorithm to decompose the graph into specified
        number of clusters (disconnected subgraphs).

        Pseudocode for the Girvan-Newman algorithm:
        -------------------------------------------
        1. Calculate the betweenness of all existing edges in the Mastodon_network.
        2. Remove the edge with the highest betweenness.
        3. Calculate the number of disconnected subgraphs.
        4. Repeat steps 1-3 until the number of disconnected subgraphs equals the predefined number of clusters.

        Parameters:
        ----------
        clusters: The number of clusters to decompose the graph into.

        Returns:
        ----------
        List of clusters, where each cluster is a list of vertices.
        """
        # Get the initial count of disconnected subgraphs
        num_clusters = len(self.get_subgraphs())

        # Loop until we have the desired number of clusters
        while num_clusters < clusters:
            # Compute shortest paths for all pairs of nodes
            self.compute_sps()

            # Identify the edge to be removed based on betweenness
            edge_to_remove = self.edge_to_remove()

            # Remove the identified edge
            self.remove_edge(edge_to_remove)

            # Update the number of disconnected subgraphs
            num_clusters = len(self.get_subgraphs())

        # Return the final clusters
        return self.get_subgraphs()

    def parse_data(self, filepath: str = 'ressources/graph_52n.json') -> None:
        """
        Parses graph data from a JSON file and populates the graph.

        Parameters:
        ----------
        filepath: Path to the JSON file containing the graph data.
        """
        # Open and read the JSON file
        with open(filepath, 'r') as file:
            data = json.load(file)

        # Remove the first key-item pair from data (if applicable)
        if data:
            first_key = list(data.keys())[0]
            del data[first_key]

        # Iterate over the data to populate vertices and edges
        for key, neighbors in data.items():
            key_user = User(key)

            # Add vertex for the user represented by 'key'
            self.add_vertex(key_user)

            # Add edges between 'key' and its neighbors
            for neighbor in neighbors:
                neighbor_user = User(neighbor)
                self.add_edge(key_user, neighbor_user)

    def show(self) -> None:
        """
        Generates and displays a visual representation of the graph.
        """
        # Initialize a Graphviz graph
        graph = graphviz.Graph(format='png', strict=True, filename='Mastodon_network')

        # Add nodes to the Graphviz graph
        for node in self.keys():
            graph.node(str(node), str(node))

        # Add edges to the Graphviz graph
        for node in self.keys():
            for target in self[node]:
                graph.edge(str(node), str(target))

        # Render the graph and create a PNG file
        graph.render()

        # Remove temporary files if needed
        os.remove('Mastodon_network')