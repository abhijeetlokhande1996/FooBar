from graph import Graph
from vertex import Vertex
import math
from copy import deepcopy


def bellManFord(g: Graph, start):
    startVertex: Vertex = g.getVertex(start)
    startVertex.setDistance(0)
    edgesArr: list = g.getEdges()
    dist = {}
    dist[start] = 0

    for i in range(g.V - 1):
        for edge in edgesArr:

            sourceId = edge[0]
            targetId = edge[1]
            weight = edge[2]

            u: Vertex = g.getVertex(sourceId)
            v: Vertex = g.getVertex(targetId)

            if u.distance != math.inf and u.distance + weight < v.distance:
                v.distance = u.distance + weight
            # if not sourceId in dist:
            #     dist[sourceId] = math.inf
            # if not destId in dist:
            #     dist[destId] = math.inf

            # if dist[sourceId] != math.inf and dist[sourceId] + weight < dist[destId]:
            #     g.getVertex(sourceId)
            #     dist[destId] = dist[sourceId] + weight

    for edge in edgesArr:
        sourceId = edge[0]
        destId = edge[1]
        weight = edge[2]

        u: Vertex = g.getVertex(sourceId)
        v: Vertex = g.getVertex(destId)
        if u.distance != math.inf and u.distance + weight < v.distance:
            return None

    return g
