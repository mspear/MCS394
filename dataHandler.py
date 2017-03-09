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
    print("number of nodes " + sizeGraph)
    sumEdges=friendGraph.number_of_edges()
    print("number of edges " + sumEdges )
    graphDensity = (2 *sumEdges)//(sizeGraph * (sizeGraph-1))
    print("density " + graphDensity)

    shortLenSum = (bfsSum(friendGraph,root))


def FWalg(graph,num):
    dist = [[-1 for x in range(num)] for y in range(num)]
    for i in num:
        dist[i][i]= 0
    for i in graph.edges():
        dist



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

