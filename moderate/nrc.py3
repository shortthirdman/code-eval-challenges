import fileinput

for line in fileinput.input():
    s = list(line.rstrip('\n'))
    t = [i for i in s if s.count(i) == 1]
    print("" if len(t) == 0 else t[0])
