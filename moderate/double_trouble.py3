import fileinput

for line in fileinput.input():
    n, r = len(line)//2, 1
    for i in range(n):
        if (line[i] == "A" and line[i+n] == "B") or (line[i] == "B" and line[i+n] == "A"):
            r = 0
            break
        elif line[i] == "*" and line[i+n] == "*":
            r *= 2
    print(r)
