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

In this problem set, you will implement a graph representing an artificial part of the Mastodon network based on the objects that you implemented in the previous week. An example can be seen below. Optionally you will 
be able to parse real world data from the Mastodon API to your graph. Based on the Graph, we will conduct a social network analysis which will require you to implement certain algorithms in order to answer questions about the network. 
In our example, a vertex represents a user located at that relative position in the network. As edges we depict connections between user. Notice that for simplicity reasons we opted for an undirected graph were there exist a connection if one of the two vertices spanning the edge follows the other. 
Furthermore the network might be a disconnected graph which means that the network comprises multiple sub-networks without a connection between them. As we depict a so called "small world network" of a user which represents all his relations, a disconnected graph is likely as you probably also have a facebook friend that is not befriended with any of your other friends.
Therefore, the program you will write can build networks that are not interconnected to one another. Which means they are only accessible separately.

<img src="/network.png" alt="network" width="570"> <br>

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
4. Execute `wget introcs.is.rw.fau.de/assets/pdfs/network.zip` to download a (compressed)
ZIP file with this problem's distribution.
5. Execute `unzip network.zip` to uncompress that file.
6. Execute `rm network.zip` followed by `yes` or `y` to delete that ZIP file.
7. Execute `ls`. You should see this problem's distribution: `network.py and main.py`
8. In order to run the `main.py` file you will have to execute the following command first in your command line: `pip3 install graphviz`

**Do not change anything in `main.py`.**

## Specification

To give you a brief overview of how we were hoping you could implement the Pythonic graph, let us look at the data 
structure you should use. 

In total, you will implement 8 methods. Notice that our provided class Graph in **network.py** inherits the properties 
of a dictionary (dict). As a result, when you have implemented your network correctly, your representation should be a 
dictionary that somewhat looks like this: 
~~~
{'Marissa': ['Sundar', 'Mark', 'Elon'], 'Sundar': ['Marissa', 'Mark', 'Elon', 'Adam', 'Jack', 'Tim', 'Emanuel'], 'Mark': ['Marissa', 'Sundar', 'Elon'], 'Elon': ['Marissa', 'Sundar', 'Adam', 'Mark'], 'Adam': ['Sundar', 'Jack', 'Elon'], 'Jack': ['Sundar', 'Adam'], 'Tim': ['Sundar'], 'Olaf': ['Emanuel', 'Rishi'], 'Emanuel': ['Olaf', 'Rishi', 'Joe', 'Sundar'], 'Rishi': ['Olaf', 'Emanuel'], 'Joe': ['Emanuel']}
~~~

**Notice that every vertex is a key in the dictionary mapped to a list of followers representing the edges.** 

**Be aware that you can not change anything about the parameters and arguments a method can take.**

### add_vertex()

Adds a vertex to the dictionary. Notice, the method only takes one argument, a key. This key is an object of the class <em>User</em> for our 
vertex in our network, i.e. the user _Mark_. When creating an object of type Graph, you create a dictionary, as you can see
from the class constructor. Thus, you will have to insert every vertex of the network as a key to your dictionary. The 
element mapped to every key/vertex in your dictionary is an empty list. Later, the edges can then be added to those lists.
For instance, if we added _Mark_, the graph vertex that we add to our graph with this method would look like this:
~~~
{Mark : []}
~~~

Hint: This is straight forward; the best implementation requires you to write a single line of code.

Hint: You can already check the correct implementation of the add function by using the check50 command in your terminal: 
check50 fau-is/IntroCS/PyGraphsTrees/Network

### add_edge()

We need this method to depict the connections between our users, i.e. the vertices in our network, as edges. This method takes two parameters. 
Firstly, ‘origin’, which is the vertex to that we add the edge. Secondly, ‘target’ is the vertex that the edge leads to 
from ‘origin’. Looking at the connection between _Sundar_ and _Adam_ in our network, the internal representation of the graph should look like this:
~~~
{Sundar : [Adam], Adam : [Sundar]}
~~~

Be careful! Since our network is an **undirected graph**, every edge goes both ways. This means that there exist a connection if only one of the two users follows the other. Thus, if we have _Adam_ as the 
origin and _Sundar_ as the target, the connection also exists vice versa. _Sundar_ can be the origin with _Adam_
as the target. When creating an edge in the method, both vertices that the edge belongs to must be added to or exist in the graph dictionary.
When the vertices exist, you can add the edge to both vertices.

Hint: You might want to sort your edges alphabetically when adding them to a vertex

### remove_edge()

We need this method to delete the connections between our users, i.e. the vertices in our network. This method will play a significant role when we detect communities in our network. 
This method should be designed analogous to the _add_vertex()_ funtion. It receives two parameters while the order of the parameters does not matter.

Later: populate the graph with our provided network in the zip file which is also used for checking your implementations or follow the instructions for populating the graph with real-time data using the Mastodon API.

### DFS

**Social-Network-Analysis:** Using the DFS algorithm we want to determine how many "sub"-networks the user _Mark_ connects.
Does Mark belong to one big community (resulting in one big connected graph) or is he part of many seperate subnetworks (many detached subnetworks)

When we create a network we want to be able to traverse our graph and discover all other vertices that
can be reached when we start at a defined vertex. For this purpose we can use a **pre-order 
depth-first search**. Therefore, the method  dfs() takes two arguments ‘start’ and “vertex=list”. 
You do not have to give a vertex list as an argument as every time this method will be called, a list will inherently 
be created. You will now have to write the pre-order depth-first search algorithm that traverses the network in a 
pre-order fashion, starting at your ‘start’ point and storing the correct path in the vertex list, returning it at 
the end of the method. 

For our example, if we started our pre-order DFS at _Mark_, the returned list ‘vertex’ should look like this:
~~~
['Mark', 'Marissa', 'Sundar', 'Elon', 'Adam', 'Jack', 'Tim', 'Emanuel', 'Olaf', 'Rishi', 'Joe']
~~~


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

### Djikstra (needs yet a use case, weighted user network regarding no of overlapping friends? Or regarding mean_time_to_next_login)

Djikstra’s algorithm allows us to calculate the shortest path between one vertex or router and any other vertex in our graph. Let us look at how the algorithm works in general.
1. For Djikstra to work, we mark our initial vertex, the one we are starting from, with a current distance of 0. The rest of the vertices are assigned distance infinity. For simplicity sakes, you can also set a value such as 9999; this suffices in our case.  
2. We now set the non-visited vertex with the smallest current distance as the current vertex X. 
3. For each neighbor N of our current vertex X, we add the current distance of our current vertex together with the weight of the edge between N and X. If the weight is smaller than the current distance to N, we set the weight as the new current distance of N. 
4. We need to mark our current vertex X as visited. 
5. If we have vertices left that are not yet visited, we go back to step ‘2’ and repeat. 

Watch this [video](https://www.youtube.com/watch?v=GazC3A4OQTE&t=362s) by Computerphile with Dr. Mike Pound of the Computer Science Department at the University of Nottingham to understand Dijkstra’s algorithm. 

Now how should Djikstra work in our graph? We want your Djikstra implementation to take a ‘start’ point and an ‘end’ point. The method should then return a tuple(x, y) with x being the shortest distance between ‘start’ and ‘end’ and y being the path you need to take from ‘start’ to ‘end’ shortest. Take as an example ‘facebook.com’ and ‘reddit.com’, which are farthest apart from one another in terms of relative distance. The return of your program should look like this:
~~~
(3, [‘facebook.com’, ‘twitter.com’, ‘instagram.com’, ‘reddit.com’])
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
check50 fau-is/IntroCS/PyGraphsTrees/Network
~~~

# submit50

To submit your program use this line of code.

~~~
submit50 fau-is/IntroCS/PyGraphsTrees/Network
~~~