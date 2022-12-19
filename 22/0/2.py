import numpy as np
T = int(input())

def solve(printers):
    mins = np.min(printers, axis=0).astype(int)
    if np.sum(mins) < 1e6:
        return "IMPOSSIBLE"
    else:
        sol = []
        for m in mins:
            sol.append(min(m, int(1e6-np.sum(sol))))
        return " ".join(map(str, sol))

for i in range(T):
    printers = []
    for _ in range(3):
        printers.append(list(map(int, input().split())))
    sol = solve(np.array(printers))
    print(f"Case #{i+1}: {sol}")