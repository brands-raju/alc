# Constant, Linear and Quadratic Space Complexity

n = 5

# 1. Constant Space - O(1)
a = 10
b = 20
total = a + b
print("Constant Space O(1):", total)

# 2. Linear Space - O(n)
numbers = []
for i in range(n):
    numbers.append(i)
print("Linear Space O(n):", numbers)

# 3. Quadratic Space - O(n^2)
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    matrix.append(row)

print("Quadratic Space O(n^2):", matrix)