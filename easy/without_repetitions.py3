import fileinput

for line in fileinput.input():
    s = list(line.rstrip('\n'))
    print(''.join([i for ix, i in enumerate(s) if ix == 0 or i != s[ix-1]]))
