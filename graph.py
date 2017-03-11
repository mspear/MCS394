import facebook
import pickle
import os
import networkx as nx
import bin.algorithms as alg


def show_graph(g):
    import matplotlib.pyplot as plt
    nx.draw_networkx(g, with_labels=False)
    plt.show()


def main():
    if os.path.isfile('/Users/mspear/graph'):
        with open('/Users/mspear/graph', 'rb') as f:
            g = pickle.load(f)
    else:
        g = facebook.make_graph()
        with open('/Users/mspear/graph', 'wb') as f:
            pickle.dump(g, f)

    cc = alg.cluster_coefficient(g)
    bc = nx.betweenness_centrality(g)
    print(bc)
    print(cc)
if __name__ == '__main__':
    main()