import numpy as np
T = int(input())

def myfunc(x):
    powers = []
    i = 1
    while i <= x:
        if i & x:
            powers.append(i)
        i <<= 1
    return powers
        
    

def is_power(n):
    return (n & (n-1) == 0) and n != 0


def solve(N):
    numbers = [2**n for n in range(30)] + list(range(300, 300 + N - 30))
    print(" ".join(map(str, numbers)))
    new_numbers = list(map(int, input().split()))
    numbers += new_numbers
    numbers = np.sort(numbers)[::-1]
    tot = np.sum(numbers)//2
    subset = []
    i = 0
    while tot>=2**30:
        num = numbers[i]
        i+=1
        if is_power(num):
            continue
        subset.append(num)
        tot -= num
    subset.extend(myfunc(tot))
    print(" ".join(map(str, subset)))

for i in range(T):
    N = int(input())
    sol = solve(N)
