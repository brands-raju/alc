
from itertools import combinations

def clique(graph, k):

    # Step 1: Get all vertices
    vertices = range(len(graph))

    # Step 2: Generate groups of k vertices
    for group in combinations(vertices, k):

        # Step 3: Assume group is a clique
        is_clique = True

        # Step 4: Check every pair of vertices
        for u, v in combinations(group, 2):

            # Step 5: Check if edge exists
            if graph[u][v] == 0:

                # Step 6: Not a clique
                is_clique = False
                break

        # Step 7: If all connections exist
        if is_clique:
            print("Clique Found:", group)
            return

    # Step 8: No clique found
    print("No Clique Found")


# Adjacency matrix
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# Required clique size
k = 3

clique(graph, k)
# Clique Algorithm finds a group of vertices in a graph where every vertex is directly connected to every other vertex. It generates different combinations of vertices 
# and checks whether all connections exist. It uses Brute Force. Its time complexity is O(C(V,k) × k²).