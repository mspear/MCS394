import graph
import facebook
#Sam Peterson is king author

def main():
    global friendGraph
    friendGraph = facebook.main()
    componentCount = 0
    global dList
    global k
    k=0
    for i in range(0,len(friendGraph)):
        dList[i]=0
    for i in dList:
        if i==0:
            k = k+1
            dfs(i, friendGraph[i])
    #k is now component count



def componentDFS(v, node):
    dList[i]=1
    neighbors = node.neighbors
    for vert in neighbors:
