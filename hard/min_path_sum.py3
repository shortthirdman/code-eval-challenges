import fileinput

n = i = 0
for line in fileinput.input():
    if n == 0:
        n = int(line)
        i, b = n, [0] * n
    else:
        s, c = [int(j) for j in line.split(',')], 0
        if i == n:
            for j in s:
                if c == 0:
                    b[0] = j
                else:
                    b[c] = b[c-1] + j
                c += 1
        else:
            for j in s:
                if c == 0:
                    b[0] += j
                else:
                    b[c] = min(b[c-1], b[c]) + j
                c += 1
        i -= 1
        if i == 0:
            print(b[n-1])
            n = 0
