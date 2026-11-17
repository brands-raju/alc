
def solve_2sat(clauses, n):

    # Step 1: Create original and reverse graphs
    graph = [[] for _ in range(2 * n)]
    rev_graph = [[] for _ in range(2 * n)]

    # Step 2: Convert literals into graph nodes
    def node(x):
        return 2 * (abs(x) - 1) + (x < 0)

    # Step 3: Add edges to both graphs
    def add_edge(u, v):
        graph[u].append(v)
        rev_graph[v].append(u)

    # Step 4: Build implication graph
    for a, b in clauses:
        u, v = node(a), node(b)

        add_edge(u ^ 1, v)
        add_edge(v ^ 1, u)

    # Step 5: Initialize visited and order
    visited = [False] * (2 * n)
    order = []

    # Step 6: First DFS
    def dfs(u):
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                dfs(v)

        order.append(u)

    # Step 7: Visit all nodes
    for i in range(2 * n):
        if not visited[i]:
            dfs(i)

    # Step 8: Initialize components
    component = [-1] * (2 * n)

    # Step 9: DFS on reverse graph
    def reverse_dfs(u, c):
        component[u] = c

        for v in rev_graph[u]:
            if component[v] == -1:
                reverse_dfs(v, c)

    # Step 10: Find SCCs
    for u in reversed(order):
        if component[u] == -1:
            reverse_dfs(u, u)

    # Step 11: Check satisfiability
    for i in range(n):
        if component[2 * i] == component[2 * i + 1]:
            print("Not Satisfiable")
            return

    print("Satisfiable")


# Clauses
clauses = [(1, 2), (-1, 2), (1, -2)]

# Number of variables
# solve_2sat(clauses, 2)
# 2-SAT is a Boolean satisfiability algorithm where each clause contains two literals. It checks whether variables can be assigned 
# True or False to satisfy all clauses. It uses an implication graph and Strongly Connected Components (SCC). Its time complexity is O(V + E).