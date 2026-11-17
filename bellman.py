
def bellman_ford(graph, V, src):

    # Step 1: Initialize all distances as infinity
    dist = [float('inf')] * V

    # Step 2: Distance of source vertex is zero
    dist[src] = 0

    # Step 3: Repeat V-1 times
    for _ in range(V-1):

        # Step 4: Check every edge
        for u, v, w in graph:

            # Step 5: Check if shorter path exists
            if dist[u] + w < dist[v]:

                # Step 6: Update distance
                dist[v] = dist[u] + w

    # Step 7: Check for negative weight cycle
    for u, v, w in graph:

        if dist[u] + w < dist[v]:
            return "Negative cycle detected"

    # Step 8: Return shortest distances
    return dist


# Graph edges: (source, destination, weight)
graph = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -2),
    (1, 3, 6),
    (2, 3, 3)
]

# V = 4 vertices, source = 0
print(bellman_ford(graph, 4, 0))
