import numpy as np

def base(N):
    """
    N: square matrix size
    generates a square matrix NxN with integer entries from 1 to N where in each column and row 
    the values are unique and in each diagonal the values are unique.
    """
    matrix = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            matrix[i, j] = (i-j) %(N) + 1
    return matrix


def solve(N, K):
    if K < N or K > N**2:
        return None
    if K%N == 0:
        ratio = K//N - 1
        matrix = base(N)
        matrix = np.roll(matrix, -ratio, axis=0)
        return matrix

    return None

def print_matrix(matrix):
    for r in matrix:
        print(" ".join(map(str,r)))

n = int(input())

def generate_all(N):
    

for i in range(n):
    N, K = input().strip().split()
    N = int(N)
    K = int(K)
    matrix = solve(N, K)
    if matrix is not None:
        print(f"Case #{i+1}: POSSIBLE")
        print_matrix(matrix)
    else:
        print(f"Case #{i+1}: IMPOSSIBLE")
