# We generate random points inside a square. We count how many points fall inside the quarter circle. Using the formula, we estimate π.
import random
def monto(n):
    inside=0
    for _ in range(n):
        x=random.random()
        y=random.random()

        if x*x + y*y<=1:
            inside+=1
    return 4*inside/n
n = 100000
print("Estimated value of Pi:", monto(n))

# Feature	Las Vegas	Monte Carlo
# Randomness	Uses random selection	Uses random numbers
# Answer	Always correct	May be approximate
# Execution time	Can vary	Usually fixed by n
# Example	Searching a number	Estimating π
# Accuracy	Guaranteed correct result	Accuracy improves with more trials

import random

def monte_carlo_coin(n):
    heads = 0

    for _ in range(n):
        toss = random.choice(["Heads", "Tails"])

        if toss == "Heads":
            heads += 1

    return heads / n


n = 10
probability = monte_carlo_coin(n)

print("Estimated probability of Heads:", probability)
