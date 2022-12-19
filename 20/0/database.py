T, B = input().split()
T = int(T)
B = int(B)

def constant(s):
    return s

def reverse(s):
    return s[::-1]

def flip(s):
    flipped = []
    for c in s:
        if c is None:
            flipped.append(None)
        else:
            flipped.append(1-c)
    return flipped

def reverse_and_flip(s):
    return flip(reverse(s))

def check_solution(s):
    if not None in s:
        print("".join([str(c) for c in s]))
        assert input() == "Y"
        return True
    return False

equals = None
diffs = None
n = 0

def query(i):
    global n
    n += 1
    print(i+1)
    return int(input())

def query_pair(i, B):
    first = query(i)
    second = query(B-i-1)
    global equals
    global diffs
    if equals == None:
        if first == second:
            equals = i
    if diffs == None:
        if first != second:
            diffs = i
    return first, second


for _ in range(T):
    equals = None
    diffs = None
    n = 0
    sol=[None for _ in range(B)]
    for i in range(5):
        sol[i], sol[B-i-1] = query_pair(i, B)
    while i<=B//2 and n<=150:
        if check_solution(sol):
            break
        if n%10 == 0:
            possible_equals = {constant, reverse, flip, reverse_and_flip}
            possible_diffs = {constant, reverse, flip, reverse_and_flip}
            if equals is not None:
                old_equal = sol[equals] 
                new_equal = query(equals)
                if old_equal == new_equal:
                    possible_equals = {constant, reverse}
                else:
                    possible_equals = {flip, reverse_and_flip}
            if diffs is not None:
                old_diff = sol[diffs]
                new_diff = query(diffs)
                if old_diff == new_diff:
                    possible_diffs = {constant, reverse_and_flip}
                else:
                    possible_diffs = {flip, reverse}
            transformation = (possible_equals & possible_diffs).pop()
            sol = transformation(sol)
            if n%10 == 1:
                query(0) # Hack to keep query in pairs
        else:
            i += 1
            sol[i], sol[B-i-1] = query_pair(i, B)