"""
Network defines a class representing the message-passing environment.

Seraphina Nix
10 February 2017
"""

import networkNode


class Network():
    """
    Creates a new Network
    """
    def __init__(self):
        # create the fields
        self.startNode = None

        # create the collections
        self.nodes = []
        self.nodeMap = {}
        self.goalNodes = []


    """
    Adds a new NetworkNode to the Network

    node: the NetworkNode to add
    """
    def addNetworkNode(self, node):
        # add the state to the network
        if node not in self.nodes:
            self.nodes.append(node)
            self.nodeMap[(node.lat, node.long)] = node


    """
    Writes the Network to a file

    filename: the name of the file in which to write the Network
    """
    def writeToFile(self, filename):
        file = open(filename, "w")

        # write the nodes to file
        file.write("Nodes:\n")
        for i in range(len(self.nodes)):
            node = self.nodes[i]
            line = "{}: {}\n".format(i, (node.lat, node.long))
            file.write(line)

        # write the edges to file
        file.write("\nEdges:\n")
        for i in range(len(self.nodes)):
            node = self.nodes[i]
            line = "{}: ".format(i)
            for j in range(len(node.neighbors)):
                neighbor = node.neighbors[j]
                if j > 0:
                    line += ", "
                line += "({}; {})".format(self.nodes.index(neighbor), round(node.costs[neighbor], 4))
            file.write("{}\n".format(line))

        # write the start node to file
        file.write("\nStart Node:\n")
        file.write("{}\n".format(self.nodes.index(self.startNode)))

        # finally, write the goal nodes to file
        file.write("\nGoal Nodes:\n")
        line = ""
        for i in range(len(self.goalNodes)):
            node = self.goalNodes[i]
            if (i > 0):
                line += ", "
            line += str(self.nodes.index(node))
        file.write("{}\n".format(line))

        # close the file
        file.close()

"""
Reads a Network from file

filename: the name of the file containing the Network
"""
def readFromFile(filename):
    # create the network to return
    net = Network()

    # read from the file
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    # process the lines
    inNodes = False
    inEdges = False
    inStart = False
    inGoals = False
    for line in lines:
        # does this line need processing?
        if (line == "\n"):
            continue
        elif (line.startswith("Nodes")):
            inNodes = True
            continue
        elif (line.startswith("Edges")):
            inNodes = False
            inEdges = True
            continue
        elif (line.startswith("Start")):
            inEdges = False
            inStart = True
            continue
        elif (line.startswith("Goal")):
            inStart = False
            inGoals = True
            continue

        # drop the newline
        line = line.replace("\n", "")

        # process the info on the line
        if (inNodes):
            split = line.split(":")
            loc = split[1]
            splitLoc = loc.replace("(", "").replace(")", "").replace(" ", "").split(",")

            nodeNum = int(split[0])
            lat = float(splitLoc[0])
            long = float(splitLoc[1])

            node = networkNode.NetworkNode(lat, long)
            net.addNetworkNode(node)
        elif (inEdges):
            split = line.split(":")
            neighbors = split[1]
            neighborsSplit = neighbors.replace(" ", "").split(",")

            nodeNum = int(split[0])
            node = net.nodes[nodeNum]
            for str in neighborsSplit:
                tupleSplit = str.replace("(", "").replace(")", "").replace(" ", "").split(";")

                neighborNum = int(tupleSplit[0])
                cost = float(tupleSplit[1])
                node.addNeighbor(net.nodes[neighborNum], cost)
        elif (inStart):
            startNum = int(line)
            net.startNode = net.nodes[startNum]
        elif (inGoals):
            line = line.replace(" ", "")
            split = line.split(",")
            for str in split:
                nodeNum = int(str)
                net.goalNodes.append(net.nodes[nodeNum])

    # return the read in network
    return net










