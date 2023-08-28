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
        # Shortest path matrix, initialized as None
        pass

    def add_vertex(self, user: object) -> None:
        """
        Adds a vertex to the graph.

        Parameters:
        ----------
        user: The user object or identifier to be added as a vertex.
        """
        # Use the string representation of the user as the key
        pass

    def add_edge(self, origin: object, target: object) -> None:
        """
        Adds an edge to the graph between `origin` and `target`.

        Parameters:
        ----------
        origin: The originating vertex.
        target: The target vertex.
        """
        pass

    def remove_edge(self, edge: Tuple[object, object]) -> None:
        """
        Removes an edge from the graph.

        Parameters:
        ----------
        edge: Tuple containing the vertices that form the edge.
        """
        pass

    def remove_vertex(self, user: object) -> None:
        """
        Removes a vertex and all its edges from the graph.

        Parameters:
        ----------
        user: The user object or identifier to be removed.
        """
        pass

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
        pass

    def get_subgraphs(self) -> List[List[str]]:
        """
        Finds disconnected subgraphs (clusters) in the graph.

        Returns:
        ----------
        List of subgraphs, where each subgraph is a list of vertices.
        """
        pass

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
        pass

    def most_influential(self) -> Tuple[str, float]:
        """
        Identifies the most influential user based on average shortest path length.

        Returns:
        ----------
        Tuple containing the most influential user and its average shortest path length.
        """
        # Create mappings from node keys to indices and vice versa

        # Initialize a matrix to store shortest paths between nodes with 'None' values

        # Populate the matrix with shortest paths between all possible node combinations

        # Initialize a dictionary to store the lengths of shortest paths for each node

        # Populate the sps_lengths dictionary with the lengths of shortest paths

        # Calculate the average shortest path length for each node

        # Identify the most influential node based on minimum average shortest path length and return both

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

        # Create list of edge pairs in the shortest path

        # Check if the given edge pair is in the shortest path

    def compute_sps(self) -> None:
        """
        Computes shortest paths between every pair of nodes and stores them in `self.sps`.
        """
        # Create mappings from node keys to indices and vice versa

        # Initialize the shortest paths matrix with 'None' values

        # Populate the shortest paths matrix

    def edge_to_remove(self) -> Tuple[str, str]:
        """
        Identifies the edge to remove based on edge betweenness.

        Returns:
        ----------
        Tuple containing the vertices of the edge to remove.
        """
        # Generate all unique pairs of nodes (potential edges)

        # Initialize a data structure to keep track of shortest path appearances for an edge

        # Calculate total number of possible shortest paths

        # Calculate edge betweenness for each pair

        # Sort edges by betweenness and return the one with highest betweenness


    def girvan_newman_algorithm(self, clusters: int) -> List[List[str]]:
        """
        Applies the Girvan-Newman algorithm to decompose the graph into specified
        number of clusters (disconnected subgraphs).

        Pseudocode for the Girvan-Newman algorithm:
        -------------------------------------------
        1. Calculate the betweenness of all existing edges in the network.
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

        # Loop until we have the desired number of clusters

            # Compute shortest paths for all pairs of nodes

            # Identify the edge to be removed based on betweenness

            # Remove the identified edge

            # Update the number of disconnected subgraphs

        # Return the final clusters

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
        graph = graphviz.Graph(format='png', strict=True, filename='network')

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
        os.remove('network')