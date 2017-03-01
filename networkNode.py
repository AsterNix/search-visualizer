"""
The NetworkNode class represents a single node in a Network.

Seraphina Nix
10 February 2017
"""

class NetworkNode():
    """
    Creates a new NetworkNode

    lat: the latitude coordinate of the NetworkNode
    long: the longitude coordinate of the NetworkNode
    """
    def __init__(self, lat, long):
        # save the params
        self.lat = lat
        self.long = long

        # create the collections
        self.neighbors = []
        self.costs = {}

    """
    Adds a NetworkNode as a neighbor

    node: the NetworkNode to add as a neighbor
    """
    def addNeighbor(self, node, cost):
        if node not in self.neighbors:
            self.neighbors.append(node)
            self.costs[node] = cost