
def floyd(g):

    # Step 1: Find number of vertices
    n = len(g)

    # Step 2: Create a copy of graph
    d = [row[:] for row in g]

    # Step 3: Consider each vertex as intermediate
    for k in range(n):

        # Step 4: Select starting vertex
        for i in range(n):

            # Step 5: Select destination vertex
            for j in range(n):

                # Step 6: Check for shorter path
                if d[i][k] + d[k][j] < d[i][j]:

                    # Step 7: Update shortest distance
                    d[i][j] = d[i][k] + d[k][j]

    # Step 8: Return final distance matrix
    return d


# Infinity means no direct connection
INF = float('inf')

# Create graph using adjacency matrix
g = [
    [0, 4, INF],
    [INF, 0, 2],
    [3, INF, 0]
]

# Print shortest distance matrix
for row in floyd(g):
    print(row)
# loyd Warshall is a shortest-path algorithm used to find the minimum distance between 
# all pairs of vertices in a graph. It checks every vertex as an
# intermediate vertex and updates distances if a shorter path exists. It uses Dynamic Programming. Its time complexity is O(n³).