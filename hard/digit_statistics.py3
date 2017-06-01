import fileinput

stats = [[2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

for line in fileinput.input():
    st = [int(s) for s in line.split()]
    st[0] -= 2
    m, res = st[1] // len(stats[st[0]]), 10 * [0]
    for i in stats[st[0]]:
        res[i] += m
    for i in range(st[1] % len(stats[st[0]])):
        res[stats[st[0]][i]] += 1
    print(', '.join([str(ix) + ": " + str(i) for ix, i in enumerate(res)]))
