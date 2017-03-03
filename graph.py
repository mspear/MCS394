import facebook
import pickle
import os
import networkx as nx


def cluster_coefficient(graph):
    cc_dict = {}
    for everynode in graph.nodes():
        g_prime = graph.subgraph([everynode]+ list(graph[everynode].keys()))
        k = nx.complete_graph(len(g_prime))
        cc_dict[everynode] = len(g_prime.edges())/len(k.edges())

    return cc_dict


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

    cc = cluster_coefficient(g)
    print(cc['https://www.facebook.com/cooper.nelson.904?fref=pb&hc_location=friends_tab'])
if __name__ == '__main__':
    main()