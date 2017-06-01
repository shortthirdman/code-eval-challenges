import fileinput

h = {}
m = [50, 25, 10, 5, 1]
def alter(n, p):
    if n == 0:
        return 1
    while m[p] > n:
        p += 1
    if m[p] == 1:
        return 1
    if not (n, p) in h:
        h[(n, p)] = alter(n - m[p], p) + alter(n, p + 1)
    return h[(n, p)]

for line in fileinput.input():
    print(alter(int(line), 0))
