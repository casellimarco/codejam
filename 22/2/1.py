import numpy as np

T = int(input())

def spiral_matrix(n):
    m = np.zeros((n, n), dtype=int)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m

def solve(i, N, K):
    if K < N - 1:
        sol = "IMPOSSIBLE"
    else:
        matrix = N**2 - spiral_matrix(N)
    
        sol = 2
    print(f"Case #{i+1}: {sol}")
    if sol != "IMPOSSIBLE":
        for i in range(sol):
            print()

for i in range(T):
    N, K = list(map(int, input().split()))
    solve(i, N, K)
