import fileinput

for line in fileinput.input():
    r = "None"
    s = line.rstrip('\n').split(',')
    n, t = len(s) // 2, set(s)
    for i in t:
        if s.count(i) > n:
            r = i
            break
    print(r)
