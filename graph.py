# class Graph:
#     def __init__(self):
#         self.g = {}
#
#     def add_node(self, node):
#         self.g[node.link] = node
#
#     def get(self, element):
#         return self.g[element]
#
#     def __contains__(self, item):
#         return item.link in self.g
#
#     def __len__(self):
#         return len(self.g)
#
#     def __iter__(self):
#         for lv in self.g:
#             yield lv
#
#
# class Node:
#     def __init__(self, name, link):
#         self.name = name
#         self.link = link
#         self.neighbors = []
#
#     def add_neighbor(self, neighbor):
#         if neighbor not in self.neighbors:
#             self.neighbors.append(neighbor)
#
#     def __hash__(self):
#         return hash(self.link)
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self.link == other.link
#         return False
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#
# def cluster_coefficient(base):
#     f = base.neighbors
#     numerator = 0
#     for friend in f:
#         numerator += (len(set(friend.neighbors).intersection(set(f))) - 1)
#     return numerator/(len(f) * (len(f)+1)/2)
import facebook
import pickle
import os
import networkx as nx


def show_graph(g):
    import matplotlib.pyplot as plt
    nx.draw_networkx(g, with_labels=False)
    plt.show()

def main():
    import operator
    if os.path.isfile('/Users/mspear/graph'):
        with open('/Users/mspear/graph', 'rb') as f:
            g = pickle.load(f)
    else:
        g = facebook.make_graph()
        with open('/Users/mspear/graph', 'wb') as f:
            pickle.dump(g, f)


    cc = nx.clustering(g)
    print(sorted(cc.items(), key=operator.itemgetter(1))[-5:])
    print(sorted(nx.betweenness_centrality(g).items(), key=operator.itemgetter(1))[-5:])
if __name__ == '__main__':
    main()