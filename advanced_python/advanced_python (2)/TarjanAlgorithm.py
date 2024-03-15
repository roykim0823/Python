
class Vertex:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.on_stack = False
        self.index = 0
        self.low_link = 0
        self.component_id = 0

    def add_neighbor(self, v):
        self.adjacency_list.append(v)

    def __str__(self):
        return '%s - %s' % (self.name, self.component_id)


class TarjanAlgorithm:

    def __init__(self, graph):
        self.graph = graph
        self.stack = []
        self.index = 0
        self.scc_counter = 0

    def find_components(self):
        for v in self.graph:
            if not v.visited:
                self.dfs(v)

    def show_components(self):
        for node in self.graph:
            print(node)

    def dfs(self, vertex):

        vertex.index = self.index
        vertex.low_link = self.index
        self.index += 1

        vertex.visited = True
        self.stack.append(vertex)
        vertex.on_stack = True

        for v in vertex.adjacency_list:
            if not v.visited:
                self.dfs(v)
                # after depth-first search we have to update the low links
                vertex.low_link = min(vertex.low_link, v.low_link)
            elif v.on_stack:
                # there is a back-edge
                vertex.low_link = min(v.index, vertex.low_link)

        if vertex.index == vertex.low_link:
            while True:
                w = self.stack.pop()
                w.on_stack = False
                w.component_id = self.scc_counter

                if w == vertex:
                    break

            self.scc_counter += 1


if __name__ == '__main__':

    v1 = Vertex('1')
    v2 = Vertex('2')
    v3 = Vertex('3')
    v4 = Vertex('4')
    v5 = Vertex('5')
    v6 = Vertex('6')
    v7 = Vertex('7')
    v8 = Vertex('8')

    v1.add_neighbor(v2)
    v2.add_neighbor(v3)
    v2.add_neighbor(v5)
    v2.add_neighbor(v6)
    v3.add_neighbor(v4)
    v3.add_neighbor(v7)
    v4.add_neighbor(v3)
    v4.add_neighbor(v8)
    v5.add_neighbor(v1)
    v5.add_neighbor(v6)
    v6.add_neighbor(v7)
    v7.add_neighbor(v6)
    v8.add_neighbor(v4)
    v8.add_neighbor(v7)

    g = [v1, v2, v3, v4, v5, v6, v7, v8]

    algorithm = TarjanAlgorithm(g)
    algorithm.find_components()
    algorithm.show_components()