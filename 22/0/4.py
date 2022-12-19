import enum

nodes = []

T = int(input())

class Node:
    def __init__(self, value):
        self.children = []
        self.value = value
        self._score = None
        self._single_score = None
        self._min_and_sum_children = None

    def __repr__(self):
        return f"Node({self.value})"
    
    def score(self):
        if self._score is None:
            min_children, sum_children = self.min_and_sum_children()
            self._score = max(self.value-min_children, 0) + sum_children
        return self._score
    
    def single_score(self):
        if self._single_score is None:
            min_children = self.min_and_sum_children()[0]
            self._single_score =  max(self.value, min_children)
        return self._single_score

    def min_and_sum_children(self):
        if self._min_and_sum_children is None:
            min_children = float('inf')
            sum_children = 0
            global nodes
            for child in self.children:
                child = nodes[child]

                min_children = min(min_children, child.single_score())
                sum_children += child.score()
            min_children = 0 if min_children == float('inf') else min_children
            self._min_and_sum_children = min_children, sum_children
        return self._min_and_sum_children

def solve(values, graph):
    global nodes
    nodes = [Node(0)] + [Node(v) for v in values]
    for i, link in enumerate(graph):
        nodes[link].children.append(i+1)
    
    return nodes[0].score() 

# import cProfile
# profiler = cProfile.Profile()
# profiler.enable()
for i in range(T):
    input()
    values = (list(map(int, input().split())))
    graph = (list(map(int, input().split())))
    
    sol = solve(values, graph)
    print(f"Case #{i+1}: {sol}")

# profiler.disable()
# filename = 'profile.prof'  # You can change this if needed
# profiler.dump_stats(filename)



