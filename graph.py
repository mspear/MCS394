class Graph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        self.g[node.link] = node

    def get(self, element):
        return self.g[element.link]

    def __contains__(self, item):
        return item.link in self.g


class Node:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __hash__(self):
        return hash(self.link)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.link == other.link
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


def main():
    g = Graph()
    tmp = Node('Test', 'https://www.facebook.com/michaela.zachman?fref=pb&hc_location=friends_tab')
    tmp.add_neighbor(Node('Hiiiiii', 'someshit'))
    g.add_node(tmp)
    tmp = Node('Other', link='https://www.facebook.com/michaela.zachman?fref=pb&hc_location=friends_tab')
    print(g.get(tmp).neighbors)

if __name__ == '__main__':
    main()