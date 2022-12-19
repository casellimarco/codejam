import numpy as np
T = int(input())

def recursive(orders, distances, removed, child_map):
    if orders.size == 0:
        print(f"Case #{i+1}: POSSIBLE")
        for mapping in removed:
            print(mapping[0], mapping[1])
        return

    child_index = np.argmin(orders[:,0])
    child = child_map[child_index]
    if 0 == orders[child_index,0]:
        next_sweet = orders[child_index,1]
        if distances[child][0] != distances[child][next_sweet]:
            print(f"Case #{i+1}: IMPOSSIBLE")
            return
    else:
        next_sweet = orders[child_index,0]
    removed.append((child+1, next_sweet+1))
    a, b = orders.shape
    orders = np.delete(orders, child_index, axis=0)
    orders = orders[orders != next_sweet]
    orders = orders.reshape(a-1, b-1)
    child_map.pop(child_index)
    
    
    recursive(orders, distances, removed, child_map)
    

                


    

def solve(coordinates, sweets):
    coordinates = np.array(coordinates)
    sweets = np.array(sweets)
    all_orders = []
    all_distances = []
    for child in coordinates:
        distances = np.sum((child - sweets)**2,axis=1)
        order = np.argsort(distances)
        all_orders.append(order)
        all_distances.append(distances)
    all_orders = np.array(all_orders)
    all_distances = np.array(all_distances)
    recursive(all_orders, all_distances, [], list(range(len(coordinates))))

for i in range(T):
    children = int(input())
    coordinates = []
    for _ in range(children):
        coordinates.append(list(map(int, input().split())))
    sweets = []
    for _ in range(children + 1):
        sweets.append(list(map(int, input().split())))

    solve(coordinates, sweets)
