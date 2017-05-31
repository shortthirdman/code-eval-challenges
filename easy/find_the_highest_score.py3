import fileinput

for line in fileinput.input():
    s, r = line.rstrip('\n').split(" | "), []
    for i in s:
        t = [int(j) for j in i.split()]
        if not r:
            r = t
        else:
            for jx, j in enumerate(t):
                if j > r[jx]:
                    r[jx] = j
    print(*r)
