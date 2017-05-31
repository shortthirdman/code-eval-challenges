import fileinput

def pos(l, lx, r, rx):
    return chr(ord(l)+lx) + chr(ord(r)+rx)

for line in fileinput.input():
    col, row, r = line[0], line[1], []
    if col > 'b' and row > '1':
        r.append(pos(col, -2, row, -1))
    if col > 'b' and row < '8':
        r.append(pos(col, -2, row, 1))
    if col > 'a' and row > '2':
        r.append(pos(col, -1, row, -2))
    if col > 'a' and row < '7':
        r.append(pos(col, -1, row, 2))
    if col < 'h' and row > '2':
        r.append(pos(col, 1, row, -2))
    if col < 'h' and row < '7':
        r.append(pos(col, 1, row, 2))
    if col < 'g' and row > '1':
        r.append(pos(col, 2, row, -1))
    if col < 'g' and row < '8':
        r.append(pos(col, 2, row, 1))
    print(*r)
