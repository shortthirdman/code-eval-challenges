import fileinput

for line in fileinput.input():
    s = line.split(' : ')
    t, u = s[0].split(), s[1].split(', ')
    for i in u:
        v = [int(j) for j in i.split('-')]
        t[v[0]], t[v[1]] = t[v[1]], t[v[0]]
    print(' '.join(t))
