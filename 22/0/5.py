from collections import Counter
from threading import TIMEOUT_MAX
import numpy as np
from scipy.stats import entropy


T = int(input())

def solve_brute_force(N, K):
    tot_E = 0
    rooms = set(range(1, N+1))
    R, E = list(map(int, input().split()))
    tot_E += E
    rooms.remove(R)
    while rooms:
        R = rooms.pop()
        print(f"T {R}")
        _, E = list(map(int, input().split()))
        tot_E += E
    
    print(f"E {tot_E//2}")

def fit(p,q):
    x = []
    y = []
    ks = []
    tot_x = np.sum(list(q.values()))
    tot_y = np.sum(list(p.values()))
    ks = [k for k in p & q]
    ks.sort()
    for k in ks:
        x.append(q[k]/tot_x)
        y.append(p[k+1]*(k+1)/tot_y)
    x = np.array(x)
    y = np.array(y)
    if True:
        quantile = max(0, 1 - 10/len(x))
        quantile = 0
        thresh =np.quantile(x, quantile)
        filter = np.logical_and(x> thresh,  y>0)
        x = x[filter]
        y = y[filter]

    x = np.array(x).reshape(-1, 1)
    mean = np.linalg.lstsq(x, y)[0]
    # import matplotlib.pyplot as plt
    # plt.plot(ks, [q[k]/tot_x for k in ks])
    # plt.plot(ks, [p[k]/tot_y for k in ks])
    # plt.savefig("distro.png")
    # plt.close()
    # plt.plot(ks, x*mean)
    # plt.plot(ks, y)
    # plt.savefig("rescaled.png")
    # print("BLA")

    return mean

def normal_mean(p,q):
    tot = 0
    mean = 0
    for k, c in p.items():
        mean += c*k
        tot += c
    for k, c in q.items():
        mean += c*k
        tot += c
    mean /= tot
    return mean
            
def get_mean(p,q):
    x = []
    y = []
    z = []
    tot_x = np.sum(list(q.values()))
    tot_y = np.sum(list(p.values()))
    for k in p | q:
        x.append(q[k]/tot_x)
        y.append(p[k]/tot_y)
        z.append(p[k+1]*(k+1)/tot_y)
    x = np.array(x).reshape(-1, 1)
    mean = np.linalg.lstsq(x, z)[0]
    z = np.array(z)/mean
    x = x.flatten()
    ent_1 = entropy(x, y)
    ent_2 = entropy(x, z)
    if ent_1 < ent_2:
        return mean
    else:
        return normal_mean(p,q)

def solve(N, K):
    p = Counter()
    q = Counter()
    rooms = set(range(1, N+1))
    R, E = list(map(int, input().split()))
    rooms.remove(R)
    p[E] += 1
    steps = 3
    for _ in range(K//(steps+1)):
        R = rooms.pop()
        print(f"T {R}")
        _, E = list(map(int, input().split()))
        p[E] += 1
        for _ in range(steps):
            print("W")
            R, E = list(map(int, input().split()))
            rooms.discard(R)
            q[E] += 1

    mean = fit(p, q)
    E = int(mean*N/2)
    print(f"E {E}")

def solve_2(N, K):
    edges = {}
    rooms = np.arange(1, N+1)
    np.random.shuffle(rooms)
    rooms = set(rooms)
    R, E = list(map(int, input().split()))
    rooms.remove(R)
    edges[R] = E
    steps = 1
    for _ in range(K//(steps+1)):
        R = rooms.pop()
        print(f"T {R}")
        _, E = list(map(int, input().split()))
        edges[R] = E
        for _ in range(steps):
            print("W")
            R, E = list(map(int, input().split()))
            rooms.discard(R)
            edges[R] = E
    mean = np.mean(list(edges.values()))
    E = int(mean*N/2)
    print(f"E {E}")


def solve_3(N, K):
    p = Counter()
    q = Counter()
    rooms = set(range(1, N+1))
    R, E = list(map(int, input().split()))
    rooms.remove(R)
    p[E] += 1
    steps = 3
    calls = 0
    while calls < K:
        R = rooms.pop()
        print(f"T {R}")
        calls+=1
        _, E = list(map(int, input().split()))
        p[E] += 1
        while calls< K:
            print("W")
            calls +=1
            R, E = list(map(int, input().split()))
            if R in rooms:
                rooms.remove(R)
                q[E] += 1
            else:
                break

    mean = normal_mean(p, q)
    E = int(mean*N/2)
    print(f"E {E}")

    

for i in range(T):
    N, K = list(map(int, input().split()))
    if N > K:
        solve_3(N, K)
    else:
        solve_brute_force(N, K)