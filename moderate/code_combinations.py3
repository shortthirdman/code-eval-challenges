import fileinput

for line in fileinput.input():
    s = line.rstrip('\n').split(" | ")
    r = 0
    for i in range(1, len(s)):
        for j in range (1, len(s[0])):
            c = sorted([s[i][j], s[i][j - 1], s[i - 1][j], s[i - 1][j - 1]])
            if ''.join(c) == "cdeo":
                r += 1
    print(r)
