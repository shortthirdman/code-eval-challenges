import fileinput

for line in fileinput.input():
    s = line.rstrip('\n').split(';')
    t, u = s[0].split(), [int(i) for i in s[1].split()]
    r = [""] * len(t)
    for ix, i in enumerate(u):
        r[i-1] = t[ix]
    for ix, i in enumerate(r):
        if i == "":
            r[ix] = t[-1]
            break
    print(' '.join(r))
