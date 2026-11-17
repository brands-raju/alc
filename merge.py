
def merge_sort(arr):

    # Step 1: Check if array has more than one element
    if len(arr) > 1:

        # Step 2: Find middle position
        mid = len(arr) // 2

        # Step 3: Divide array into two halves
        left = arr[:mid]
        right = arr[mid:]

        # Step 4: Sort both halves recursively
        merge_sort(left)
        merge_sort(right)

        # Step 5: Initialize three pointers
        i = j = k = 0

        # Step 6: Compare elements of both halves
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # Step 7: Copy remaining elements from left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Step 8: Copy remaining elements from right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


# Take input from user
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

print("Original array:", arr)

merge_sort(arr)

print("Sorted array:", arr)
# Time Complexity	O(n log n)
# Why O(n log n)?
# - Dividing the array takes log n levels.
# - Merging at each level takes O(n) time.
# - Therefore, total time = O(n log n)