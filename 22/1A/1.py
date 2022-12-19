T = int(input())

def solve(word):
    count = []
    previous = None
    for letter in word:
        if previous == letter:
            count[-1][-1] += 1
        else:
            count.append([letter, 1])
        previous = letter
    sol = ""
    for i, c in enumerate(count[:-1]):
        sol += c[0]*c[1] 
        if c[0] < count[i+1][0]:
            sol += c[0]*c[1] 
    sol += count[-1][0]*count[-1][1]

    return sol

for i in range(T):
    word = input()
    sol = solve(word)
    print(f"Case #{i+1}: {sol}")
