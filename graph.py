class Graph:
    def __init__(self):
        self.g = []

    def add_node(self, node):
        self.g.append(node)


class Node:
<<<<<<< HEAD
    def __init__(self, id, name):
        #self.id = id
=======
    def __init__(self, name):
>>>>>>> 0ff4dba7dcb162737d1cf35e866185b9619e120e
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
