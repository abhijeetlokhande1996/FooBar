from vertex import Vertex


class Graph:
    def __init__(self):
        self.adjacencyList = {}
        self.V = 0

    def addVertex(self, id):
        self.V += 1
        nv = Vertex(id)
        self.adjacencyList[id] = nv

    def addEdge(self, source, dest, weight=0):
        if source not in self.adjacencyList:
            self.addVertex(source)
        if dest not in self.adjacencyList:
            self.addVertex(dest)

        sourceVertex: Vertex = self.adjacencyList[source]
        sourceVertex.addNeighbour(dest, weight)

    def getVertex(self, id):
        if id in self.adjacencyList:
            return self.adjacencyList[id]
        return None

    def getVertexList(self):
        return list(self.adjacencyList.keys())

    def getEdges(self):
        edgeArr = []
        for vName in list(self.adjacencyList.keys()):
            vertex: Vertex = self.adjacencyList[vName]
            for nbr in list(vertex.connectedTo.keys()):
                edgeArr.append(
                    (vName, nbr, vertex.connectedTo[nbr]))
        return edgeArr

    def __str__(self):
        return f"{str(list(self.adjacencyList.keys()) )}"
