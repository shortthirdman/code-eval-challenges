import fileinput

for line in fileinput.input():
    s = [int(i) for i in line.translate({ord(i):None for i in 'VampiresZobWtchHu: \n'}).split(',')]
    print(0 if s[0] + s[1] + s[2] == 0 else (s[0] * 3 + s[1] * 4 + s[2] * 5) * s[3] // (s[0] + s[1] + s[2]))
