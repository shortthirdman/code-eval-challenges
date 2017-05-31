import fileinput

for line in fileinput.input():
    s = line.split(" | ")
    t = [int(i) for i in s[0].split()]
    n, l = int(s[1]), 1
    for _ in range(n):
        p, l = l, 0
        for j in range(p, len(t)):
            if t[j] < t[j-1]:
                t[j], t[j-1] = t[j-1], t[j]
                l = j - 1 if j > 1 else 2
                break
        if l == 0:
            break
    print(' '.join([str(i) for i in t]))
