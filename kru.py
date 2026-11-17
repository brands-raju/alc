
def kruskal(edges, n):

    parent = list(range(n))

    total = 0

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:

        if find(u) != find(v):

            print(u, "-", v, ":", w)

            total += w

            parent[find(u)] = find(v)

    print("Minimum Cost:", total)


edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(edges, 4)
# Kruskal's algorithm finds the Minimum Spanning Tree.
# It sorts all edges from smallest weight to largest weight.
# It selects the smallest edge if it does not form a cycle.
# It stops after selecting n - 1 edges.