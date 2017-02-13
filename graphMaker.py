import turtle
import facebook
import graph

class Vertex:
    def __init__(self, friends, location):
        self.friends = friends
        self.loc = location

def main():
    turtle1 = turtle.Turtle()
    #run the facebook data puller to create the graph
    graphMaker(turtle1, graph.Graph())
    return

def graphMaker(turtle1, graph):
    #I'm assuming the michael spear user is the first entry in graph.g list and will be center of graph
    vertexDict={}
    vertexDict["Michael Spear"]=[graph.g[0],0.0,0.0] #alright so this is kinda awful but currently im storing the node with
    #its location where x is at index 1 and y at index 2
    turte1.dot(10,"black")
    turtle1.up()
    turtle1.speed(10)
    turtle1.goto(300,0)
    turtle1.setheading(90)
    for i in range(1,42): #doing this bc as far as i know we are just doing the 40 other friends
        current = graph.g[i]
        #i'm assuming we can pull the names from the facebook data and that this name is unique and the same as the
        #the names in the neighbors lists
        turtle1.left(9)
        turtle1.forward(25)
        x,y = turtle1.pos()
        vertexDict[current.name]=[graph.g[i],x,y]
        turtle1.dot(10,black)
    #ok so i've drawn the nodes now i need to connect them
    for i in vertexDict:
        node1,x,y = i
        turtle1.goto(x,y)
        turtle1.down()
        for j in node1.neighbors:
            n,x1,y1=vertexDict[j.name]
            turtle1.goto(x1,y1)
            turtle1.goto(x,y)
    return
