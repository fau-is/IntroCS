# Week 2: Understanding Relationships with Graphs and Trees
## Objective
To help students understand graphs and trees as well as their benefits using the relationships between different users, posts, retweets, and favourites.
## Tasks (high level):
1. Understanding Graphs & Trees: Students will receive a lecture about the basic concepts.
2. Graph Implementation: Students will design a graph where nodes represent the entities (users, posts, retweets, favourites), and edges represent the relationships between these entities.
3. Tree Implementation: Students will also create a binary tree for storing retweets efficiently. Each retweet can be stored in the binary tree using the alphabetical order of the user who retweeted.
4. Traversal Algorithms: Students will implement and understand various graph and tree traversal algorithms such as Depth First Search (DFS), Breadth-First Search (BFS), in-order, pre-order, and post-order tree traversal.
5. Performance Analysis: Students will analyse the time and space complexity of their implementations. They will also discuss the efficiency and real-world applicability of their chosen data structures.
## Tasks for (user) graph (low level):

1. Determine if the graph of users G is connected or contains disconnected subgraphs. For this you should implement an iterative/recursive Depth-First-Search algorithm that traverses over the graph in a DFS-manner. It should return a list of visited nodes in the order of traversal.
2. Determine if there exist a mediate connection between two users A and B. Implement an iterative/recursive Breadth-First-Search algorithm that traverses over the graph in a BFS-manner. The BFS algorithm not only finds a connection, it also finds the shortest path in case of an unweighted graph.
3. Identify the most influential user based on the "Closeness measure" which requires you to compute shortest paths via BFS or Dijkstra. Additionally, answer the following question: "On average, through how many corners are you connected to every other person in the network?"
>  **Closeness**: Average length of the shortest paths between that node and all other nodes in the graph.
4. Community Detection: Using the Girvan Newman algorithm, identify the three clusters describing the three most dense communities in the graph.

### Variants

1. Identify the most influential user based on the "Betweeness measure" which requires you to compute shortest paths via BFS or Dijkstra. 
>  **Betweeness**: Number of shortest paths from all nodes to all others that pass through a particular node.
2. Find the most influential user based on the amount of followers (edges branching off)
3. Community Detection via Density measure: Using the Density measure, identify the three clusters describing the three most dense communities in the graph.
> **Density Measure**: This measures the number of existing links over the possible number of links within a group of nodes. A higher density indicates a stronger community
4. (not yet implemented) Cycle Detection: Identify users who retweeted a retweet of their own post. For this you will need to apply the DFS algorithm to detect cycles in a social network graphs. 