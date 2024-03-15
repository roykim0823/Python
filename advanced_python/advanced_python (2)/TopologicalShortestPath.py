import sys

MAX_VALUE = sys.maxsize


class Vertex:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.min_distance = MAX_VALUE
        self.predecessor = None
        self.adjacency_list = []

    def add_neighbor(self, v):
        self.adjacency_list.append(v)

    def __str__(self):
        return '%s - %s' % (self.name, self.predecessor)


class Edge:

    def __init__(self, target, weight):
        self.target = target
        self.weight = weight


class TopologicalOrdering:

    def __init__(self, graph):
        # it stores all the vertices of the G(V,E) graph
        self.graph = graph
        self.stack = []

        for vertex in graph:
            if not vertex.visited:
                self.dfs(vertex)

    def dfs(self, v):
        v.visited = True

        for neighbor in v.adjacency_list:
            if not neighbor.target.visited:
                self.dfs(neighbor.target)

        self.stack.append(v)

    def get_topological_order(self):
        return self.stack


class ShortestPath:

    def __init__(self, graph):
        self.graph = graph
        self.graph[0].min_distance = 0
        self.topological_ordering = TopologicalOrdering(graph)

    def compute(self):
        stack = self.topological_ordering.get_topological_order()

        while stack:
            u = stack.pop()

            for edge in u.adjacency_list:
                v = edge.target

                # relaxation
                if u.min_distance + edge.weight < v.min_distance:
                    v.min_distance = u.min_distance + edge.weight
                    v.predecessor = u


if __name__ == '__main__':
    v0 = Vertex('S')
    v1 = Vertex('A')
    v2 = Vertex('B')
    v3 = Vertex('C')
    v4 = Vertex('D')
    v5 = Vertex('E')

    v0.adjacency_list.append(Edge(v1, 1))
    v0.adjacency_list.append(Edge(v3, 2))

    v1.adjacency_list.append(Edge(v2, 6))

    v2.adjacency_list.append(Edge(v4, 1))
    v2.adjacency_list.append(Edge(v5, 2))

    v3.adjacency_list.append(Edge(v1, 4))
    v3.adjacency_list.append(Edge(v4, 3))

    v4.adjacency_list.append(Edge(v5, 1))

    g = [v0, v1, v2, v3, v4, v5]

    algorithm = ShortestPath(g)
    algorithm.compute()

    for node in g:
        print('Distance from s: %s - %s' % (node.min_distance, node))
