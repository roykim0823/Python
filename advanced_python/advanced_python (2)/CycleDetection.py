
class Vertex:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.being_visited = False
        self.adjacency_list = []

    def add_neighbor(self, v):
        self.adjacency_list.append(v)

    def __str__(self):
        return self.name


class CycleDetection:

    def __init__(self, graph):
        self.graph = graph

    def detect_cycles(self):
        for v in self.graph:
            if not v.visited:
                self.dfs(v)

    def dfs(self, vertex):
        vertex.being_visited = True

        for v in vertex.adjacency_list:
            if v.being_visited:
                print('We have found a negative cycle...')
                return

            if not v.visited:
                v.visited = True
                self.dfs(v)

        vertex.visited = True
        vertex.being_visited = False


if __name__ == '__main__':
    v0 = Vertex('A')
    v1 = Vertex('B')
    v2 = Vertex('C')
    v3 = Vertex('D')
    v4 = Vertex('E')
    v5 = Vertex('F')

    v5.add_neighbor(v0)
    v0.add_neighbor(v4)
    v0.add_neighbor(v2)
    # v4.add_neighbor(v5)
    v2.add_neighbor(v1)
    v2.add_neighbor(v3)

    g = [v0, v1, v2, v3, v4, v5]

    algorithm = CycleDetection(g)
    algorithm.detect_cycles()
