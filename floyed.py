INF = 99999999

n = int(input("Enter number of vertices "))
g = []

for i in range(n):
    t = []
    for j in range(n):
        if i != j:
            weight = int(input(f"Enter the weight between the nodes (Enter -1 for no path) {i} and {j} "))
            if weight != -1:
                t.append(weight)
            else:
                t.append(INF)
        else:
            t.append(0)
    g.append(t)



def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance


ans = floyd_warshall(g)


def print_solution(distance):
    for i in range(n):
        for j in range(n):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

print_solution(g)




# zerone: space complexity: O(nW) and time complexity: O(nW)
# fracknap: space complexity: O(n) and time complexity: O(n log n)
# huffman: space complexity: O(n) and time complexity: O(n log n)
# queen1: space complexity: O(n) and time complexity: O(n!)
# queen2: space complexity: O(n^2) and time complexity: O(n!)
# graphcol: space complexity: O(V) and time complexity: O(V+E)
# matrixchain: space complexity: O(n^2) and time complexity: O(n^3)
# tspbb: space complexity: O(n^2) and time complexity: O(n^2 * 2^n)
# lcs: space complexity: O(mn) and time complexity: O(mn)
# zeronebb: space complexity: O(n) and time complexity: O(2^n)
# floyed: space complexity: O(n^2) and time complexity: O(n^3)
# tspdp: space complexity: O(n * 2^n) and time complexity: O(n^2 * 2^n)
# jobseq: space complexity: O(n) and time complexity: O(n log n)
# dijkstra: space complexity: O(V^2) and time complexity: O(V^2)
# kruskal: space complexity: O(E) and time complexity: O(E log V)
# prims: space complexity: O(V+E) and time complexity: O(E logV)
# bellman: space complexity: O(V) and time complexity: O(VE)