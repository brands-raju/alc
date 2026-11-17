
from itertools import product

def solve_3sat(clauses, n):

    # Step 1: Generate all True/False combinations
    for values in product([False, True], repeat=n):

        # Step 2: Assume all clauses are true
        result = True

        # Step 3: Check every clause
        for clause in clauses:

            # Step 4: Initially clause is not satisfied
            satisfied = False

            # Step 5: Check every literal
            for literal in clause:

                # Step 6: Get variable value
                variable = values[abs(literal) - 1]

                # Step 7: Check negative literal
                if literal < 0:
                    variable = not variable

                # Step 8: If any literal is true
                if variable:
                    satisfied = True
                    break

            # Step 9: If a clause is false
            if not satisfied:
                result = False
                break

        # Step 10: If all clauses are true
        if result:
            print("Satisfiable")
            print("Assignment:", values)
            return

    # Step 11: No valid assignment found
    print("Not Satisfiable")


# Given clauses
clauses = [
    (1, 2, -3),
    (-1, 2, 3),
    (1, -2, 3)
]

# Number of variables
solve_3sat(clauses, 3)
# 3-SAT is a Boolean satisfiability problem where each clause contains three literals. It checks all possible True and False combinations of variables to 
# find an assignment that satisfies every clause. It uses the Brute Force technique. Its time complexity is O(m × 2ⁿ).