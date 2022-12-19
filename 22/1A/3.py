import numpy as np
T = int(input())
from itertools import zip_longest, permutations
from functools import lru_cache

@lru_cache(128)
def dist(ex1, ex2):
    for i, (a,b) in enumerate(zip_longest(ex1, ex2)):
        if a != b:
            return max(0,len(ex1)-i)+max(0,len(ex2)-i)
    return 0

def solve_next(string, strings):
    if len(strings) == 0:
        return len(string)
    string2 = strings[0]
    min_cost = np.inf
    for s2 in set(permutations(string2, len(string2))):
        cost = dist(string, s2)
        cost += solve_next(s2, strings[1:])
        min_cost = min(cost, min_cost)
    return min_cost


def solve(exercises):
    strings = []
    exercises = np.array(exercises)
    min =  np.min(exercises, axis=0)
    exercises = exercises - min
    for exercise in exercises:
        string = "".join([str(i)*v for i, v in enumerate(exercise)])
        strings.append(string)
    return solve_next("", strings) + np.sum(min)*2


def solve2(exercises):
    exercises = np.array(exercises)
    C={}
    for i in range(len(exercises)):
        for j in range(i, len(exercises)):
            C[(i,j)] = np.min(exercises[i:j+1], axis=0).sum()
    @lru_cache(10000)
    def M(l,r):
        if l == r:
            return 0
        else:
            min_v = np.inf
            for x in range(l,r):
                min_v = min(min_v, M(l,x) + M(x+1,r) + 2*(C[(l,x)] + C[(x+1,r)] - 2*C[(l,r)]))
            return min_v
    # for s in range(1,len(exercises)):
    #     for l in range(len(exercises)-s):
    #         M(l,l+s)
     
    return M(0,len(exercises)-1) + 2*C[(0,len(exercises)-1)]
    
import cProfile, pstats
profiler = cProfile.Profile()
profiler.enable()
for i in range(T):
    E, W = list(map(int, input().split()))
    exercises = []
    for _ in range(E):
       exercises.append(list(map(int, input().split()))) 
    
    sol = solve2(exercises)
    print(f"Case #{i+1}: {sol}")
profiler.disable()
filename = 'profile.prof'
profiler.dump_stats(filename)
