import numpy as np
T = int(input())

def totale(N):
    full = 0
    for x in range(0, N+1):
        x_square = x**2
        N_square = (N+1/2)**2 
        for y in range(x):
            if x_square + y**2 <= N_square:
                full += 1
    return 8*full

def solve(N):
    radii = np.arange(N + 1)**2
    tot = set()
    for x in range(0, N+1):
        diff = radii - x**2
        diff = diff[diff >= 0]
        ys = np.unique(np.round(np.sqrt(diff)).astype(int))
        tot.update(set([(x,y) for y in ys]))
        tot.update(set([(y,x) for y in ys]))
    wrong = 4*len(tot) #- 2*(2*N+1)  -1
    return totale(N) - wrong
for i in range(T):
    N = int(input())
    sol = solve(N)
    print(f"Case #{i+1}: {sol}")
