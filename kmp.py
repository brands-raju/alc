def kmp(s,p):
    lps=[0] * len(p)
    j=0

    for i in range(1,len(p)):
        while j and p[i]!=p[j]:
            j=lps[j-1]
        if p[i]==p[j]:
            j+=1
        lps[i]=j

    j=0
    for i in range(len(s)):
        while j and s[i]!=p[j]:
            j=lps[j-1]
        if s[i]==p[j]:
            j+=1
        if j == len(p):
            return i-j+1
    return -1

print(kmp("ababcabcabababd","ababd"))

# What is KMP?

# Knuth-Morris-Pratt (KMP) is a string-matching algorithm used to find a pattern inside a larger text.

# It avoids unnecessary character comparisons by using an LPS array.

# Example:
# - Text: ABABDABACDABABCABAB
# - Pattern: ABABCABAB
# The algorithm searches for the pattern and finds its first occurrence at index 10.
# Complexity	Value
# Time Complexity	O(n + m)
# Space Complexity	O(m)
# Where:
# - n = length of text.
# - m = length of pattern.