import fileinput

for line in fileinput.input():
    s, o = int(line) - 1, ord('A')
    d = chr(s % 26 + o)
    while s >= 26:
        s = s // 26 - 1
        d = chr(s % 26 + o) + d
    print(d)
