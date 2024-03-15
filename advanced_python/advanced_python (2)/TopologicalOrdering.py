
class Vertex:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.neighbors = []

    def add_neighbor(self, v):
        self.neighbors.append(v)

    def __str__(self):
        return self.name


class TopologicalOrdering:

    def __init__(self):
        self.stack = []

    def dfs(self, v):

        v.visited = True

        # this is the standard depth-first search
        for neighbor in v.neighbors:
            if not neighbor.visited:
                self.dfs(neighbor)

        self.stack.append(v)

    def show_ordering(self):
        while len(self.stack) != 0:
            print(self.stack.pop())


if __name__ == '__main__':

    graph = [Vertex('0'), Vertex('1'), Vertex('2'), Vertex('3'), Vertex('4'), Vertex('5')]

    graph[2].add_neighbor(graph[3])
    graph[3].add_neighbor(graph[1])
    graph[4].add_neighbor(graph[0])
    graph[4].add_neighbor(graph[1])
    graph[5].add_neighbor(graph[0])
    graph[5].add_neighbor(graph[2])

    ordering = TopologicalOrdering()

    # there may be independent clusters
    # or there may be unreachable vertexes because of directed edges
    for vertex in graph:
        if not vertex.visited:
            ordering.dfs(vertex)

    ordering.show_ordering()

