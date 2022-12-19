from collections import defaultdict
T = int(input())

def solve(R,C):
    first_line = ".."+"+-"*(C-1) + "+"
    print(first_line)
    second_line = ".." + "|."*(C-1) + "|"
    print(second_line)
    first_line = "+-" + first_line[2:]
    second_line = "|" + second_line[1:]
    for _ in range(R-1):
        print(first_line)
        print(second_line)
    print(first_line)


for i in range(T):
    R, C = input().split()
    R = int(R)
    C = int(C)
    print(f"Case #{i+1}:")
    solve(R, C)