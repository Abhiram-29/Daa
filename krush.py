import heapq

def kruskal_mst(graph):
    edges = []
    for u, v, weight in graph:
        edges.append((weight, u, v))

    edges.sort()
    heapq.heapify(edges)

    parent = {node: node for node in range(len(graph) + 1)}
    rank = {node: 0 for node in range(len(graph) + 1)}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1

    mst = []
    while edges:
        weight, u, v = heapq.heappop(edges)
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))

    return mst

# Example usage
graph = [(0, 1, 2), (0, 3, 6), (1, 3, 8), (1, 2, 3), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
mst = kruskal_mst(graph)
print("Edges in the constructed MST")
print("(Node1, Node2, Weight)")
for u, v, weight in mst:
    print(f"({u}, {v}, {weight})")