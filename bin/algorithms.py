import networkx as nx

def cluster_coefficient(graph):
    cc_dict = {}
    for everynode in graph.nodes():
        g_prime = graph.subgraph([everynode]+ list(graph[everynode].keys()))
        k = nx.complete_graph(len(g_prime))
        cc_dict[everynode] = len(g_prime.edges())/len(k.edges())

    return cc_dict


def main():
    g = nx.Graph()
    g.add_path([1, 2, 3, 4, 5, 6, 7, 8])
    g.add_path([9, 8, 10])
    


if __name__ == '__main__':
    main()