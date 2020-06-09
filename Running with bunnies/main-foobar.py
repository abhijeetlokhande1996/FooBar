from graph import Graph
from bellmanFord import bellManFord
from copy import deepcopy


def bellManFordCompleteSource(g: Graph):
    distList: list = []
    vertexList = list(g.adjacencyList.keys())
    for idx, source in enumerate(vertexList):
        ans: Graph = bellManFord(deepcopy(g), source)
        if not ans:
            return None
        arrToAdd = []
        for vid in ans.adjacencyList.keys():
            arrToAdd.append(ans.getVertex(vid).distance)
        distList.append(deepcopy(arrToAdd))
    return distList


def getPath(dist, start, goal, time, n):
    stack = [(start, [start], time, [[i] for i in range(n)])]
    childVertex = set(range(n))

    while stack:
        (vertex, path, remainTime, cycleFactorVertexes) = stack.pop()

        for next in childVertex - set(cycleFactorVertexes[vertex]):
            timeToNext = dist[vertex][next]
            timeToBackFromNext = dist[next][vertex]

            timeToGoalFromNext = dist[next][goal]
            nextCycleFactorVertexes = deepcopy(cycleFactorVertexes)
            if timeToNext + timeToBackFromNext == 0:
                nextCycleFactorVertexes[vertex].append(next)
                nextCycleFactorVertexes[next].append(vertex)

            if remainTime - timeToNext - timeToGoalFromNext >= 0:
                nextPath = path + [next]
                nextRemainTime = remainTime - timeToNext
                stack.append((next, nextPath, nextRemainTime,
                              nextCycleFactorVertexes))

                if next == goal:
                    freedBunnies = set(nextPath)
                    yield freedBunnies
                    if len(freedBunnies) == n:
                        return


def main(sm, timeLimit):
    g = Graph()

    for idx, row in enumerate(sm):
        for idy, col in enumerate(row):
            g.addEdge(idx, idy, col)

    if g.V < 3:
        return []

    distList: list = bellManFordCompleteSource(deepcopy(g))
    maxFreedBunnies = set([])
    if distList:
        for freedBunnies in getPath(dist=distList, start=0, goal=len(sm)-1, time=timeLimit, n=len(sm)):

            maxLen = len(maxFreedBunnies)
            freedLen = len(freedBunnies)
            if maxLen < freedLen or (maxLen == freedLen and sum(maxFreedBunnies) > sum(freedBunnies)):
                maxFreedBunnies = freedBunnies

    else:
        #print("Negative cycle detected")
        return list(range(g.V-2))

    ans = list(map(lambda x: x-1, maxFreedBunnies - set([0, len(sm)-1])))
    return ans


sm = [[0, 2, 2, 2, -1],
      [9, 0, 2, 2, -1],
      [9, 3, 0, 2, -1],
      [9, 3, 2, 0, -1],
      [9, 3, 2, 2, 0]]

timeLimit = 1
main(sm, timeLimit)
