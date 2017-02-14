class Graph:
    def __init__(self):
        self.g = []

    def add_node(self, node):
        self.g.append(node)


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)