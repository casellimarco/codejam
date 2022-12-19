with open("4.in", "a") as f:
    f.write("10000\n")
    f.write(" ".join(["10" for _ in range(10000)]) + "\n")
    f.write(" ".join(["0 1 2 3 4" for _ in range(10000//5)]) + "\n")