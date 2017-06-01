import fileinput

def slide(a):
    lastNum, lastNumID, lastZero = -1, -1, -1
    for i in range(len(a)):
        if a[i] == 0:
            if lastZero == -1:
                lastZero = i
        elif lastNum == a[i]:
            a[lastNumID] = 2 * lastNum
            lastNum = -1
            a[i] = 0
            if lastZero == -1:
                lastZero = i
        else:
            lastNum = a[i]
            if lastZero == -1:
                lastNumID = i
            else:
                lastNumID = lastZero
                a[lastZero] = a[i]
                a[i] = 0
                lastZero += 1
    return a

for line in fileinput.input():
    s = line.split("; ")
    n = int(s[1])
    m = [[int(j) for j in i.split()] for i in s[2].split('|')]
    for i in range(n):
        if s[0] == "LEFT":
            m[i] = slide(m[i])
        elif s[0] == "RIGHT":
            m[i].reverse()
            m[i] = slide(m[i])
            m[i].reverse()
        elif s[0] == "UP":
            l = slide([m[j][i] for j in range(n)])
            for j in range(n):
                m[j][i] = l[j]
        elif s[0] == "DOWN":
            l = slide([m[j][i] for j in range(n - 1, -1, -1)])
            for j in range(n):
                m[j][i] = l[n - j - 1]
    print('|'.join([' '.join([str(j) for j in i]) for i in m]))
