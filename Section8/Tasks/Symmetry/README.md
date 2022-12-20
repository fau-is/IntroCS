# Graph Drawing
## Lab Setup
Before we start hacking, you need to execute a few commands:
´´´
sudo apt install graphviz
pip install graphviz
´´´
If prompted whether you want to use up more space just type 'y' and hit Enter. Don't worry about any warnings.
To test if the installation worked, run:
´´´
python graph_drawer.py
´´´
If no error shows up, you're good to go!

{% next "Lab Setting" %}

Imagine, after finishing IntroCS successfully you apply for an internship at a large software vendor "Geeglo".
"Geeglo" likes to ask algorithmic questions in job interviews.
As you arrive for your interview, they ask you to write a function which determines if a graph is undirected or directed.
The graph is encoded as a Python graph.
The lab provided comes with three files:
- symmetry.py => This is where you need to add your symmetry check.
- symmetry_test.py => Unit-test cases for the function you need to write
- graph_drawer.py => When you're finished it should draw an undirected graph.

Based on an adjacency matrix, the function in _symmetry.py_ will determine if the set of edges is symmetric or not.

**If you feel comfortable already, try to solve the task from here.**

**Exam mode - finish the task in at most 10 minutes.**

{% next "Undirected vs. Directed" %}
You recall the IntroCS week of Graphs and Trees.
You remember that directed graphs are graphs which allow walking along the edges in a single direction.
In contrast, in undirected graphs every edge can be walked along in both directions.

You remember:
```
If every edge exists in both directions, then the set of edges is symmetric.
```
**If you feel comfortable already, try to solve the task from here.**

{% next "Adjacency Matrices" %}
Now that you remembered the conditions for undirected graphs, you recall the functionality of adjacency matrices.

An adjacency matrix is an _n x n matrix_. It represents a graph with exactly _n_ vertices indicated by row or column
in the matrix.
Consequently, an adjacency matrix only contains information about all edges in the matrix.
Some conditions which account in an adjacency matrix:
* If _matrix[0][2] == 0: Then, there is no connection from node _0_ to node _2_
* If _matrix[0][1] > 0_: Then, there is an edge from node _0_ to node _1_
* If _matrix[1][0] > 0_: Then, there is an edge from node _1_ to node _0_
* If _matrix[1][0] == _matrix[0][1] Then, the edges from node 1 to node 0 and node 0 to node 1 are symmetric.

**Even if all information did not suffice for you to solve the task, take a minute to think about the indication.**

{% spoiler "Further Hints" %}
How to solve the task:
* set up a double for-loop (each going to range(len(matrix)))
* Let's take a look at the decisive condition:
    * If _matrix[1][0] == _matrix[0][1] Then, the edges from node 1 to node 0 and node 0 to node 1 are symmetric.
    * Let's replace the indices: If _matrix[row][column] == matrix[column][row]_ then an edge is symmetric
    * Use the double for loop to check this condition for every fiel

{%endspoiler%}







