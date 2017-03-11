import graph
import facebook
import pickle
import networkx as nx
import os
import stack
import queue
#Sam Peterson is king author

 def main():
     global friendGraph
     friendGraph = pickle.load("FILE")


   #  root = friendGraph.node('https://www.facebook.com/michael.spear.94')

  #   sizeGraph = friendGraph.number_of_nodes()
  #   print("number of nodes " + sizeGraph)
 #    sumEdges=friendGraph.number_of_edges()
 #    print("number of edges " + sumEdges )
 #    graphDensity = (2 *sumEdges)//(sizeGraph * (sizeGraph-1))
#     print("density " + graphDensity)

#     shortLenSum = (bfsSum(friendGraph,root))


    root = friendGraph.node('https://www.facebook.com/michael.spear.94')

    sizeGraph = friendGraph.number_of_nodes()
    print("number of nodes: " + sizeGraph)
    sumEdges=friendGraph.number_of_edges()
    print("number of edges: " + sumEdges )
    graphDensity = (2 *sumEdges)//(sizeGraph * (sizeGraph-1))
    print("density: " + graphDensity)
    fwDict = FWalg(friendGraph)
    averagePathLenth = lG(fwDict, sizeGraph)
    print("average path length: " + averagePathLenth)


def lG(dict1, num):
    acc= 0
    for i in dict1:
        for j in dict1:
            if i != j:
                acc = dict1[i][j]
    averageLength = (1/(num*(num-1))) * acc
    return averageLength


def FWalg(graph):
    dist = {}
    for i in graph:
        dist[i] = dict([(j, float('inf')) for j in graph if i != j])
    for i in dist:
        dist[i][i] = 0
    for i in dist:
        for j in graph[i]:
            dist[i][j] = 1
    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def betweenCentr(vertex,graph):
    CBV = 0
    for s in graph:
        S = stack.Stack()
       # return nx.betweeness_centrality(graph)
        #P[w] = empty list, w is a member of V
        A=dict([(j,0) for j in graph])
        A[s] = 1
        d = [-1 for i in len(graph)]






#def bfsSum(graph,r):
 #   sum = 0
  #  newDict = {}


    #componentCount = 0
    #global dList
    #global k
    #k=0
    #for i in range(0,len(friendGraph)):
     #   dList[i]=0
    #for i in dList:
     #   if i==0:
      #      k = k+1
       #     dfs(i, friendGraph[i])
    #k is now component count



#def componentDFS(v, node):
 #   dList[i]=1
  #  neighbors = node.neighbors
   # for vert in neighbors:

def main():
    import pickle
    import datetime
    with open('/Users/mspear/graph', 'rb') as f:
        g = pickle.load(f)
    t = datetime.datetime.now()
    FWalg(g)
    t2 = datetime.datetime.now()
    nx.average_shortest_path_length(g)
    t3 = datetime.datetime.now()
    print(t2 - t)
    print(t3 - t2)
    # for key, value in FWalg(g).items():
    #     print(key, value)
