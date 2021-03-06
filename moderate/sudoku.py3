import fileinput

sq = {4: 2, 9: 3}

def region(a, n):
    x, y = a % n, a // n
    return x // sq[n] + sq[n] * (y // sq[n])

for line in fileinput.input():
    s = line.split(';')
    g = [int(i) for i in s[1].split(',')]
    n = int(s[0])
    valid = True
    row, col, reg = [0] * n, [0] * n, [0] * n
    for ix, i in enumerate(g):
        if row[ix // n] & 1 << i:
            valid = False
            break
        row[ix // n] |= 1 << i
        if col[ix % n] & 1 << i:
            valid = False
            break
        col[ix % n] |= 1 << i
        if reg[region(ix, n)] & 1 << i:
            valid = False
            break
        reg[region(ix, n)] |= 1 << i
    print("True" if valid else "False")
