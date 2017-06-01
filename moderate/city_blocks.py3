import fileinput

for line in fileinput.input():
    s = line.translate({ord(i):None for i in '()'}).split()
    p = [float(i) for i in s[0].split(',')]
    q = [float(i) for i in s[1].split(',')]
    if len(p) < 2 or len(q) < 2:
        print(0)
        continue
    if p[0] != 0:
        p = [i - p[0] for i in p]
    if q[0] != 0:
        q = [i - q[0] for i in q]
    ins, stl, avl = 0, p[-1], q[-1]
    q = [i * stl / avl for i in q]
    i = j = 0
    while i < len(p) and j < len(q):
        if p[i] == q[j]:
            ins += 1
            i += 1
            j += 1
        elif p[i] < q[j]:
            i += 1
        else:
            j += 1
    print(len(p) + len(q) - ins - 1)
