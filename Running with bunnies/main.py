from graph import Graph
from bellmanFord import bellManFord
g = Graph()
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# g.addEdge(1, 2, 4)
# g.addEdge(1, 4, 5)
# g.addEdge(2, 4, 5)
# g.addEdge(4, 3, 2)
# g.addEdge(3, 2, -10)

# Negative Cycle
# g.addEdge(0, 1, 1)
# g.addEdge(3, 0, -1)
# g.addEdge(2, 3, -1)
# g.addEdge(1, 2, -1)

# g.addEdge("A", "B", 4)
# g.addEdge("A", "C", 2)
# g.addEdge("B", "C", 3)
# g.addEdge("B", "D", 2)
# g.addEdge("B", "E", 3)
# g.addEdge("C", "B", 1)
# g.addEdge("C", "E", 5)
# g.addEdge("C", "D", 4)
# g.addEdge("E", "D", -5)

# g.addEdge(0, 1, 5)
# g.addEdge(0, 2, 4)
# g.addEdge(1, 3, 3)
# g.addEdge(2, 1, 6)
# g.addEdge(3, 2, 2)

dist = bellManFord(g, 0)
print(dist)
