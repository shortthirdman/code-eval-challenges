import fileinput

def ismagic(a):
    d, ns, r = [False for _ in range(10)], [], 0
    while a > 0:
        r = a % 10
        if r == 0 or d[r]:
            return False
        d[r] = True
        ns.append(r)
        a //= 10
    d, r = [False for _ in range(len(ns) + 1)], 1
    for _ in range(len(ns)):
        r = (r + ns[-r]) % len(ns)
        if r == 0:
            r = len(ns)
        if d[r]:
            return False
        d[r] = True
    return r == 1

maxb, magic = 0, []
for line in fileinput.input():
    s, r = [int(i) for i in line.split()], []
    while s[1] > maxb:
        maxb += 1
        if ismagic(maxb):
            magic.append(maxb)
    for i in magic:
        if i < s[0]:
            continue
        if i > s[1]:
            break
        r.append(i)
    print(" ".join([str(i) for i in r]) if r else -1)
