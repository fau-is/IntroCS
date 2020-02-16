from collections import defaultdict


class Graph(object):

    # sth is an adjacency list in the form [node, directed_edge]
    def __init__(self, sth):
        if sth is not None:
            self.sth = sth

        # init dictionary for easier use of adjacency list
        self.adj = defaultdict(list)
        # for every node there is a key in the dictionary
        for idx, elem in enumerate(sth):
            # the values in the dictionary are the nodes, to which a directed edge exists
            for i in elem:
                self.adj[idx].append(i)

    # if an edge is added to the graph, you only need to insert the end of the edge into the list of directed edges from the starting node
    def add(self, start, end):
        self.adj[start].append(end)

    # calls the dfs_helper() function for the actual execution of the dfs algorithm. This could also be done in only one function.
    def dfs(self, root, tofind):
        nbr, path, found = self.dfs_helper(root, tofind)
        if found:
            return nbr, path
        else:
            return -1, []

    # iterative dfs implementation
    # takes: root -> node to start the dfs from
    #        tofind -> node that is looked for
    def dfs_helper(self, root, tofind):
        # explicit stack for iterative implementation
        stack = []

        # like specified: return the number of nodes that your DFS crossed until you found the element
        # and the path it took there as list of nodes
        # number of nodes visited to the goal
        number = 0
        # the path your dfs took through the graph
        path = []

        # init stack with the start node (i.e. root)
        stack.insert(0, root)
        # init found with bottom, because node is not yet found
        found = False

        # while there are still nodes left that can be visited do...
        while stack:
            # take first element form the stack
            cur = stack.pop(0)
            # append first element to the path (because path is essentially your set of visited nodes)
            path.append(cur)

            # if the node is found -> search is finished
            if cur == tofind:
                found = True
                break

            # else, search continues and the number of steps is incremented
            number = number + 1

            # this is equivalent of the recusive call of dfs on every child node.
            for child in self.adj[cur]:
                # equivalent to: if child was not yet visited
                if child not in path:
                    # put child into the stack of nodes that still need to be processed.
                    stack.insert(0, child)

        # found is for you calling method to know if the dfs succeeded
        # path is the path you took through the graph
        # number is the number of steps through the graph
        # the redundancy here could be discussed
        return number, path, found

# example of an input [node, directed_edge] -> this notation means, that the first dimension is the node and the second dimension is the nodes, to which a directed edge exits
if __name__ == '__main__':

    # draw this graph to assure yourself of the result
    # question: which direction will the dfs take through the graph? (depends on the use of the stack)
    graph = Graph([
        [1,2],
        [],
        [1,3,4],
        [],
        []])

    number, path = graph.dfs(0,4)
    print(number)
    print(path)