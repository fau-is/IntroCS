# Network
{:.no_toc}

Networks are omnipresent in our increasingly connected world. We use logistical networks to determine the fastest way from A to B, social networks to interact with friends, or Wide Area Networks like the Internet in many areas of daily life such as communication, entertainment, shopping, education, etc.

Network theory has emerged in science to capture, describe and explore these and many other phenomena of our time. It is used in various disciplines such as sociology, psychology, healthcare, neuroscience, as well as almost all natural sciences where it is part of graph theory.

Computer science is a special field of application because it can support many other disciplines through digital network representations in computationally intensive analyses. Network theory is therefore an interdisciplinary interface for us, allowing us to apply our previously acquired IntroCS knowledge to a new field of research.
In this assignment, we want to specifically deal with social network analysis, a subfield of sociology. SNA provides us with tools to decipher and visualize relationships and information flows between people, groups, organizations, or other networked units.
It can provide answers to exciting questions such as:

- "How polarized is a voter network?"
- "How fragmented is a consumer network?"
- "How do people's world views might differ as a consequence of what they see, read, and hear in their feeds?"
- "What assumptions about a city's culture and social composition can we infer by comparing networks from people living in different locations?"

These insights from sociology, psychology, economics, and society can help us to view the world in a more nuanced way and to make progressive decisions based on it.

In this problem set, you will implement a graph representing a personal network of a Mastodon user. While exercises are described based on an artificial example (displayed below) you will 
directly apply your implementation to real world data from the Mastodon API. Based on the established Graph and algorithms we will be able to conduct a social network analysis which answers questions about a network. 
In our graph, a vertex represents a user located at that relative position in the network. As edges we depict connections between user. Notice that for simplicity reasons we opted for an undirected graph where there exist a connection if one of the two vertices spanning the edge follows the other. 
Furthermore the network might be a disconnected graph which means that the network comprises multiple sub-networks without a connection between them. A disconnected graph is likely in real world data as you probably also have a facebook friend that is not befriended with any of your other friends.
Therefore, the program you will write can build networks that are not interconnected to one another.

<p align="center">
<img src="network_web.png" alt="network" width="570"> <br>
</p>

***

* TOC
{:toc}

***

## Getting Started

Log into the [CS50 IDE](https://cs50.dev/) and then, in a terminal window,
execute each of the below

1. Execute `cd` to ensure that you're in `~/` (i.e., your home directory).
2. Execute `mkdir Graphs_Trees` to make (i.e., create) a directory called `Graphs_Trees` in
your home directory.
3. Execute `cd Graphs_Trees` to change into that directory
4. Execute `wget introcs.is.rw.fau.de/assets/pdfs/mastodon_network.zip` to download a (compressed)
ZIP file with this problem's distribution.
5. Execute `unzip network.zip` to uncompress that file.
6. Execute `rm network.zip` followed by `yes` or `y` to delete that ZIP file.
7. Execute `ls`. You should see this problem's distribution: `graph.py, network_analysis.py and a ressources directory`
8. In order to run the `network_analysis.py` file you will have to execute the following command first in your command line: `pip3 install graphviz`

**Do not change anything in `network_analysis.py`. This is a script that you can use to test your graph.py implementation. Do also not change anything the ressources directory.**

## Specification

To give you a brief overview of how we were hoping you could implement the Pythonic graph, let us look at the data 
structure you should use. 

Notice that our provided class Graph in **graph.py** inherits the properties 
of a dictionary (dict). As a result, when you have implemented your network correctly, your representation should be a 
dictionary that somewhat looks like this: 
~~~
{'Marissa': ['Sundar', 'Mark', 'Elon'], 'Sundar': ['Marissa', 'Mark', 'Elon', 'Adam', 'Jack', 'Tim', 'Emanuel'], 'Mark': ['Marissa', 'Sundar', 'Elon'], 'Elon': ['Marissa', 'Sundar', 'Adam', 'Mark'], 'Adam': ['Sundar', 'Jack', 'Elon'], 'Jack': ['Sundar', 'Adam'], 'Tim': ['Sundar'], 'Olaf': ['Emanuel', 'Rishi'], 'Emanuel': ['Olaf', 'Rishi', 'Joe', 'Sundar'], 'Rishi': ['Olaf', 'Emanuel'], 'Joe': ['Emanuel']}
~~~

**Notice that every vertex is a key in the dictionary mapped to a list of followers representing the edges.** 

**Be aware that you can not change anything about the parameters and arguments a method can take.**

We divided this exercise into 5 separate logical chapters which together require the implementation of **12 methods** in total. Notice that 2 auxiliary methods are already given to you.
- **parse_data()**: parses real world data from Mastodon to your graph implementation
- **show()**: uses the graphviz library to visualizes your graph by creating a png-file. You can always execute this method to check the current state of your graph.

Let us now start with the first chapter...

## 1. Graph implementation

### add_vertex()

Adds a vertex to the dictionary. Notice, the method only takes one argument, a key. This key is an object of the class <em>User</em> for our 
vertex in our network, i.e. the user _Mark_. When creating an object of type Graph, you create a dictionary, as you can see
from the class constructor. Thus, you will have to insert every vertex of the network as a key to your dictionary. The 
element mapped to every key/vertex in your dictionary is an empty list. Later, the neighbors can then be added to those lists.
For instance, if we added _Mark_, the graph vertex that we add to our graph with this method would look like this:
~~~
{Mark : []}
~~~

Hint: This is straight forward; the best implementation requires you to write a single line of code.

### add_edge()

We need this method to depict the connections between our users, i.e. the vertices in our network, as edges. This method takes two parameters. 
Firstly, ‘origin’, which is the vertex to that we add the edge. Secondly, ‘target’ is the vertex that the edge leads to 
from ‘origin’. Looking at the connection between _Sundar_ and _Adam_ in our network, the internal representation of the graph should look like this:
~~~
{Sundar : [Adam], Adam : [Sundar]}
~~~

When creating an edge in the method, both vertices that the edge belongs to must be added to or exist in the graph dictionary. 
Be careful! Since our network is an **undirected graph**, every edge goes both ways. This means that there exist a connection if only one of the two users follows the other. Thus, if we have _Adam_ as the 
origin and _Sundar_ as the target, the connection also exists vice versa. _Sundar_ can be the origin with _Adam_
as the target. **Important**: You should sort your edges alphabetically when adding them to a vertex.

### remove_edge()

We need this method to delete the connections between our users, i.e. the vertices in our network. This method will play a significant role when we detect communities in our network. 
This method should be designed analogous to the _add_edge()_ funtion. It receives two parameters while the order of the parameters does not matter.

### remove_vertex()

Like for edges we also need a method that removes a vertex from the graph. Make sure to handle all its edges that still exist with this vertex accordingly.

**Hint: You can now check the correct implementation of the add- and remove-functions by using the check50 command in your terminal:**
~~~
check50 fau-is/IntroCS/Mastodon_GT/Mastodon_network
~~~
**With these four methods we are now able to populate the graph with our provided network in the json format. Exercise 1.1 in network_analysis.py should run properly and generate a png file of the Mastodon network.**

## 2. Network Connectivity (DFS)


### Depht-First-Search (DFS)

When we create a network we want to be able to traverse our graph and discover all other vertices that
can be reached when we start at a defined vertex. For this purpose we can use a (pre-order) **depth-first search**. Therefore, the method  dfs() takes one argument ‘start’. 
You will now have to write the pre-order depth-first search algorithm that traverses the network in a 
pre-order fashion, starting at your ‘start’ point and storing the correct path in a list of visited vertices, returning it at 
the end of the method. 

For our example, if we started our pre-order DFS at _Mark_, the returned list ‘vertex’ should look like this:
~~~
['Mark', 'Elon', 'Adam', 'Jack', 'Sundar', 'Emanuel', 'Joe', 'Olaf', 'Rishi', 'Marissa', 'Tim']
~~~

**Sub-Networks: Identifying Disconnected Clusters**

In this section, your task is to use the Depth-First Search (DFS) algorithm to figure out how many separate "sub-networks"
or clusters are in our graph. These sub-networks represent groups of vertices that are connected to each other but not to
vertices in other sub-networks. This is important in understanding whether a Mastodon user's network forms one large interconnected community or consists of several smaller, isolated groups.

Your task is to write the get_subgraphs() method. This method should identify and return all the disconnected clusters within the graph.
Each cluster (or sub-network) is represented as a list of vertices that are connected to each other.
If the graph is fully connected (meaning there are no isolated clusters), your method should return a list containing
just one item, which is a list of all vertices in the graph.

To achieve this, you'll first need to implement a DFS method as described earlier. Then, using this DFS method, you can
explore the graph from each vertex that hasn't been visited yet, finding all vertices that are part of the same cluster.
Each time you find a new cluster, add it to your list of subgraphs. This way, you'll end up with a list of all the separate 
clusters in the graph.

Hint: We recommend using the python's set() built-in.


### BFS

**Social-Network-Analysis:** Find the shortest path connecting two users in the network using BFS (with path tracking)

When we create a network we want to be able to specify the shortest path connecting two vertices. While Dijkstra is a suitable algorithm when we face weighted graphs, BFS finds the shortest path in unweighted graphs.
Therefore, you will now implement a **breadth-first search** with path-tracking.
The method takes two arguments, a ‘start’ vertex and an 'end' vertex.
The function should return a vertex list with all the vertices belonging to the identified shortest path including the start and end vertices. 
So take once again our starting point _Mark_ and the end vertex _Jack_ the shortest path should look like this:
~~~
['Mark', 'Sundar', 'Jack']
~~~


### Most influential user
Next we want to identify the most influential user in a network. There are many interpretations of influential and even more techniques to calculate them. In this task we determine the degree of influence based on a "Closeness" measure.
By calculating the "Closeness" measure for every node we can additionally answer one of the most respected questions in network theory researched by Milgram et al as the [Small-world experiment](https://en.wikipedia.org/wiki/Small-world_experiment) "On average, through how many corners are you connected to every other person in the network?" This task requires you to implement the Dijkstra algorithm (if graph is  weighted based on mean_time_to_next_login) or BFS for shortest path identification.
> Closeness: average length of the shortest paths between that node and all other nodes in the graph

### Community detection
Finally, we want to detect communities within the network using the Girvan Newman Algorithm which requires you to calculate a betweenness measure for your network edges
> Betweenness: Number of shortest paths from all nodes to all others that pass through a particular edge

> **Girvan Newman Algorithm:** steps for community detection:
    1. The betweenness of all existing edges in the network is calculated first.
    2. The edge(s) with the highest betweenness are removed.
    3. The betweenness of all edges affected by the removal is recalculated.
    4. Steps 2 and 3 are repeated until no edges remain.

We therefore ask you to implement the following functions:
- _get_subgraphs()_
- _compute_shortest_paths()_
- _edge_to_remove()_
- _edge_in_sp()_
- _get_communities()_

# check50

To check your program you can run this line in your terminal.
~~~
check50 fau-is/IntroCS/Mastodon_GT/mastodon_network
~~~

# submit50

To submit your program use this line of code.

~~~
submit50 fau-is/IntroCS/Mastodon_GT/mastodon_network
~~~