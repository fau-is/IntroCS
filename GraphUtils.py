class User():
    def __init__(self, username):
        self.username = username


class Edge():
    def __init__(self, user1, user2, weight=None):
        self.user1 = user1
        self.user2 = user2
        self.weight = weight


class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = []

    def build_graph(self, path):
        # Iterate through json
        # json = pd.read_json()
        # add user
        self.add_user(username)

        # add edge
        self.add_edge(user1,user2)

    def add_user(self, username):
        user = User(username)
        self.nodes.append(user)

    def add_edge(self, user1, user2):
        edge = Edge(user1, user2)
        self.edges.append(edge)


    g = Graph("data.csv")

    g = Graph()
    g.build_graph("data.csv")


