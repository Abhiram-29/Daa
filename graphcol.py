class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_neighbors(self, vertex):
        return self.graph[vertex]

def graph_coloring(graph):
    colors = {}
    vertices = graph.get_vertices()
    for vertex in vertices:
        neighbors = graph.get_neighbors(vertex)
        available_colors = set(range(len(vertices)))
        for neighbor in neighbors:
            if neighbor in colors:
                available_colors.discard(colors[neighbor])
        if available_colors:
            colors[vertex] = min(available_colors)
        else:
            raise ValueError("No available colors for vertex: " + str(vertex))
    return colors

def main():
    graph = Graph()

    print("Enter edges (e.g., 'u v' for an edge between u and v):")
    num_edges = int(input("Enter number of edges: "))
    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    try:
        coloring = graph_coloring(graph)
        print("Graph coloring:")
        s = []
        for vertex, color in coloring.items():
            print("Vertex:", vertex, "Color:", color)
            if color not in s:
                s.append(color)
        print("Chromatic number: ",len(s))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()