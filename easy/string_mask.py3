import fileinput

for line in fileinput.input():
    s = line.split()
    print(''.join([i.lower() if s[1][ix] == "0" else i.upper() for ix, i in enumerate(s[0])]))
