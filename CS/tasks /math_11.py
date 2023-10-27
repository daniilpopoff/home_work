def find_solutions():
    solutions = []
    f = 0
    while len(solutions) != 1:
        f += 1
        for a in range(1, f):
            for b in range(1, f):
                for c in range(1, f):
                    for d in range(1, f):
                        if a**2 + b**3 + c**5 + d**7 == f**11:
                            solutions.append((a, b, c, d, f))
                            if len(solutions) == 3:
                                return solutions
    return solutions

solutions = find_solutions()
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    print(f"a = {solution[0]}")
    print(f"b = {solution[1]}")
    print(f"c = {solution[2]}")
    print(f"d = {solution[3]}")
    print(f"f = {solution[4]}")