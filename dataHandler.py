import graph
import facebook
import pickle
import networkx as nx
import os
#Sam Peterson is king author

def main():
    global friendGraph
    friendGraph = pickle.load("FILE")


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


#def bfsSum(graph,r):
 #   sum = 0
  #  newDict = {}


    componentCount = 0
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

