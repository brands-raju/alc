def rabin(s,p):
    n,m=len(s),len(p)

    h=hash(p)

    for i in range(n-m+1):
        if hash(s[i:i+m])==h and s[i:i+m]==p:
            return i
    return -1
print(rabin("hello world", "world"))
#What is Rabin-Karp Algorithm?

# Rabin-Karp is a string-matching algorithm that uses hash values to search for a pattern inside a larger text.

# Important concepts:
# - Hashing: Converts a string into a numerical hash value.
# - Pattern: String that we want to find.
# - Substring: A smaller part of the main text.
# - Hash collision: When two different strings produce the same hash value.
# Complexity	Value
# Time	O((n-m+1) × m) average
# Space	O(m)

# Note: This supplied code recalculates each substring's hash. The optimized Rabin-Karp algorithm uses a rolling hash to improve searching efficiency.