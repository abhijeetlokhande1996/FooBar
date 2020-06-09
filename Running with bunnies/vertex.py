import math


class Vertex:
    def __init__(self, id):
        self.id = id
        self.connectedTo = {}
        self.distance = math.inf

    def getDistance(self):
        return self.distance

    def setDistance(self, d):
        self.distance = d

    def getId(self):
        return self.id

    def addNeighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnectionList(self):
        return list(self.connectedTo.keys())

    def __str__(self):
        return f"{self.id} connected to {str(list(self.connectedTo.items()))}"
