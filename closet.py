
import math

# Step 1: Calculate distance between two points
def dist(p1, p2):
    return math.sqrt(
        (p1[0]-p2[0])**2 +
        (p1[1]-p2[1])**2
    )


# Step 2: Brute force for small number of points
def brute(points):
    return min(
        (dist(points[i], points[j]), (points[i], points[j]))
        for i in range(len(points))
        for j in range(i+1, len(points))
    )


# Step 3: Closest pair function
def closest(points):

    # Step 4: Base case
    if len(points) <= 3:
        return brute(points)

    # Step 5: Divide points into two halves
    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]

    # Step 6: Find closest pair in both halves
    d1, p1 = closest(left)
    d2, p2 = closest(right)

    # Step 7: Choose smaller distance
    d, pair = (d1, p1) if d1 < d2 else (d2, p2)

    # Step 8: Create strip near middle line
    strip = [
        p for p in points
        if abs(p[0]-points[mid][0]) < d
    ]

    # Step 9: Sort strip by y-coordinate
    strip.sort(key=lambda p: p[1])

    # Step 10: Check points inside strip
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):

            # Stop if vertical difference is too large
            if strip[j][1]-strip[i][1] >= d:
                break

            # Calculate distance
            d2 = dist(strip[i], strip[j])

            # Update minimum distance
            if d2 < d:
                d, pair = d2, (strip[i], strip[j])

    return d, pair


# Step 11: Take number of points
n = int(input("Enter number of points: "))

# Step 12: Take x and y coordinates
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# Step 13: Check minimum points
if n < 2:
    print("At least two points required")

else:

    # Step 14: Sort points by x-coordinate
    points.sort()

    # Step 15: Find closest pair
    d, pair = closest(points)

    print("Closest pair:", pair)
    print("Minimum distance:", round(d, 2))
# Closest Pair of Points finds the two points having the minimum distance between them. It divides the points into two halves, finds the closest pair in each half, and 
# checks points near the middle strip. It uses Divide and Conquer. Its time complexity for your given code is O(n log² n).