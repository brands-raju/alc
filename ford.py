def ford(cap,s,t):
    n=len(cap)
    flow=0
    while True:
        parent=[-1] *n
        parent[s]=s
        q=[s]
        for u in q:
            for v in range(n):
                if parent[v]==-1 and cap[u][v] >0:
                    parent[v]=u
                    q.append(v)
        if parent[t]==-1:
            break
        f=float('inf')
        v=t

        while v !=s:
            u=parent[v]
            f=min(f,cap[u][v])
            v=u
        v=t
        while v!=s:
            u=parent[v]
            cap[u][v]-=f
            cap[v][u]+=f
            v=u
        flow+=f
    return flow
# Capacity graph
cap = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

# Source = 0, Sink = 5
print("Maximum Flow:", ford(cap, 0, 5))

# BFS: Finds an available path.
# Parent: Remembers the previous node.
# f: Stores the minimum capacity of a path.
# Residual capacity: Remaining capacity after sending flow.
# Reverse capacity: Allows previously sent flow to be redirected if needed.
# Flow: Total amount sent from source to sink.
# Complexity	Value
# Time	O(V × E²)
# Space	O(V²)

# Here, V = number of vertices and E = number of edges. The time complexity is for this BFS-based Ford-Fulkerson implementation (Edmonds-Karp).