import random 
def las(arr,key):
    while True:
        x=random.choice(arr)
        if x==key:
            return x
        else:
            return -1
arr = [10, 20, 30, 40, 50]
key = 30

result = las(arr, key)

if result != -1:
    print("Number found:", result)
else:
    print("Number not found")
# - It uses random selection.
# - The answer is always correct.
# - Running time may vary.
# - It keeps searching until the target is found (if the target exists).
# Remember: Las Vegas = Always correct answer, variable running time