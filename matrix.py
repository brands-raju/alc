def matrix(p):
    n=len(p)-1
    dp=[[0]*n for _ in range(n)]

    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1
            dp[i][j]=float('inf')
            for k in range(i,j):
                cost=(
                    dp[i][k]
                    +dp[k+1][j]
                    +p[i]*p[k+1]*p[j+1]
                )
                dp[i][j]=min(dp[i][j],cost)
    return dp[0][n-1]
# Matrix dimensions
p = [10, 20, 30, 40, 30]

print("Minimum number of multiplications:",
      matrix(p))
# To implement the Matrix Chain Multiplication algorithm using Dynamic Programming to find the minimum number of scalar multiplications required to multiply a sequence of matrices.
# We cannot change the order of matrices, but we can change the brackets (parentheses).

# For example:
# 1. ((A1 × A2) × A3) × A4
# 2. (A1 × A2) × (A3 × A4)
# 3. A1 × (A2 × (A3 × A4))
# All give the same final matrix, but their multiplication costs are different.

# Our aim: Find which bracket arrangement requires the minimum number of scalar multiplications.