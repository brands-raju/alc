
def prim(graph):

    n = len(graph)

    selected = [False] * n

    selected[0] = True

    total = 0

    for _ in range(n - 1):

        minimum = float('inf')

        x = y = -1

        for i in range(n):

            if selected[i]:

                for j in range(n):

                    if not selected[j] and graph[i][j] != 0:

                        if graph[i][j] < minimum:

                            minimum = graph[i][j]

                            x, y = i, j

        print(x, "-", y, ":", minimum)

        total += minimum

        selected[y] = True

    print("Minimum Cost:", total)


graph = [
    [0, 2, 3, 0],
    [2, 0, 1, 4],
    [3, 1, 0, 5],
    [0, 4, 5, 0]
]

prim(graph)
# Prim's: Start from one node and grow the tree.
# Kruskal's: Sort all edges and select the smallest ones.