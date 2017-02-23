class Graph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        self.g[node.link] = node

    def get(self, element):
        return self.g[element.link]

    def __contains__(self, item):
        return item.link in self.g

    def __len__(self):
        return len(self.g)

    def __iter__(self):
        for lv in self.g:
            yield lv


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

def cluster_coefficient(base):
    f = base.neighbors
    numerator = 0
    for friend in f:
        numerator += (len(set(friend.neighbors).intersection(set(f))) - 1)
    return numerator


def main():
    import facebook
    import pickle
    import os
    if os.path.isfile('/Users/mspear/graph'):
        g = pickle.load('/Users/mspear/graph')
    else:
        g = facebook.main()

    cc = [cluster_coefficient(g.get(lv))/len(g) for lv in g]
    cc.sort()
    print(*(lv for lv in cc[-1: -5]), sep='\n')
if __name__ == '__main__':
    main()