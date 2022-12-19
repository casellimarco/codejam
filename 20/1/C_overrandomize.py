
from collections import Counter


T = int(input())

for i in range(T):
    _ = input()
    c  = Counter()
    digits = set()

    for _ in range(10**4):
        _, R =input().split()
        c.update(R[0])
        digits |= set(R)
    zero = (digits - c.keys()).pop()
    sol = zero + "".join([k for k,v in c.most_common()])
	
    print(f"Case #{i+1}: {sol}")
