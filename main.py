class Dijkstra:
    def __init__(self, graph):
        self.weight = None
        self.graph = graph

    def minimal_weight(self, start, end, added_weight=0):
        for v in [v for v in self.graph if v.start == start]:
            new_weight = v.weight + added_weight
            weight_from_subpath = self.minimal_weight(v.end, end, new_weight)

            if self.weight is not None and new_weight > self.weight:
                return self.weight

            if v.end == end and (self.weight is None or new_weight < self.weight):
                self.weight = new_weight

            if weight_from_subpath is not None and (self.weight is None or weight_from_subpath < self.weight):
                self.weight = weight_from_subpath

        return self.weight


class Vector:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


if __name__ == '__main__':
    dijkstra = Dijkstra([
        Vector(start='A', end='B', weight=6),
        Vector(start='B', end='C', weight=4),
        Vector(start='B', end='C', weight=8),
        Vector(start='A', end='C', weight=12)
    ])

    print(dijkstra.minimal_weight('A', 'C'))
