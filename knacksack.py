def knack(weights,values,capacity):
    n=len(weights)
    dp=[[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<=w:
                dp[i][w]=max(
                    values[i-1]+dp[i-1][w-weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] =dp[i-1][w]

    return dp[n][capacity]

weights = [3, 4, 5, 6]
values = [3, 4, 5, 6]
capacity = 5

print("Maximum value:", knack(weights, values, capacity))

# . Basic concept (4 lines)
# 1. 0/1 Knapsack is an algorithm used to select items to get the maximum total value.
# 2. Every item has a weight and a value.
# 3. We have a fixed bag capacity, so the total weight cannot exceed that capacity.
# 4. Each item can be selected only once (1) or not selected (0).
# Simple example: You have a bag with capacity 5 kg. You have four items, and you must choose the items that give you the maximum value without exceeding 5 kg.