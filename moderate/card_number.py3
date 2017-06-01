import fileinput

for line in fileinput.input():
    s = [int(i) for i in line if i.isdigit()]
    for i in range(len(s)-2, -1, -2):
        s[i] *= 2
        if s[i] > 9:
            s[i] = s[i] % 10 + 1
    print(1 if sum(s) % 10 == 0 else 0)
