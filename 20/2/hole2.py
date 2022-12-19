from collections import defaultdict
from fractions import Fraction
T = int(input())

for i in range(T):
    N = int(input())
    holes = []
    for h in range(N):
        holes.append(tuple(map(int, input().split())))
        
    c = defaultdict(set)
    for h1 in holes:
        for h2 in holes:
            if h1 != h2:
                
                dx = h1[0] - h2[0]
                dy = h1[1] - h2[1]
                if dy == 0 :
                    diff = "inf"
                else:
                    diff = Fraction(dx, dy)
                c[diff].add(h1)
                c[diff].add(h2)
    max_set = set()
    for k, v in c.items():
        if len(v) > len(max_set):
            max_set = v
    l = len(max_set)//2*2
    head_and_tail = min(N- l,2)
    sol = l + head_and_tail
    print(f"Case #{i+1}: {sol}")