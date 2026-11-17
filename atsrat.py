
import heapq

def astar(graph, start, goal):

    h = {'A': 4, 'B': 3, 'C': 1, 'D': 0}

    pq = [(h[start], start)]

    cost = {start: 0}
    parent = {start: None}

    while pq:

        _, u = heapq.heappop(pq)

        if u == goal:
            path = []
            while u:
                path.append(u)
                u = parent[u]

            return path[::-1], cost[goal]

        for v, w in graph[u]:

            new_cost = cost[u] + w

            if new_cost < cost.get(v, float('inf')):

                cost[v] = new_cost
                parent[v] = u

                f = new_cost + h[v]

                heapq.heappush(pq, (f, v))

    return [], -1


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

path, cost = astar(graph, 'A', 'D')

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)

# To implement the A* algorithm in Python to find the shortest path between a starting node and a goal node using actual cost and heuristic cost.
# Actual cost (g): Cost already travelled from the starting node.
# Heuristic cost (h): Estimated cost remaining to reach the goal.