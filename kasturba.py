def karatsuba(x, y):

    # Base case: small numbers
    if x < 10 or y < 10:
        return x * y

    # Find the number of digits
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split both numbers into two parts
    power = 10 ** m
    a, b = divmod(x, power)
    c, d = divmod(y, power)

    # Three recursive multiplications
    z0 = karatsuba(b, d)
    z2 = karatsuba(a, c)
    z1 = karatsuba(a + b, c + d) - z2 - z0

    # Combine the results
    return z2 * (10 ** (2 * m)) + z1 * power + z0


# Test with large integers
x = 123456789
y = 987654321

result = karatsuba(x, y)

print("First number:", x)
print("Second number:", y)
print("Karatsuba result:", result)
print("Correct result:", x * y)

# Karatsuba is an algorithm used to multiply large numbers.
# It divides each number into two smaller parts.
# It uses 3 recursive multiplications instead of 4.
# Finally, it combines the results to get the final answer.