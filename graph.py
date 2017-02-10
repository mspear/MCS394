class Graph:
    def __init__(self):
        self.g = []

    def add_node(self, id, name):
        self.g.append(Node(id, name))

    def __contains__(self, item):
        for V in self.g:
            if V.id == item:
                return True

        return False
class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)