import fileinput

for line in fileinput.input():
    s = line.split(" | ")
    t, m = s[0].split(), int(s[1])
    while len(t) > 1:
        n = m % len(t) - 1
        del t[n]
    print(t[0])
