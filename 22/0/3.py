import numpy as np
T = int(input())

def solve(dices):
    dices.sort()
    sol = 0
    for d in dices:
        if d>sol:
            sol += 1
    return sol

for i in range(T):
    input()
    dices = (list(map(int, input().split())))
    sol = solve(dices)
    print(f"Case #{i+1}: {sol}")