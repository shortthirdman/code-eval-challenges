import fileinput

m = ["Done", "Low", "Medium", "High", "Critical"]

def prio(a):
    if a == 0:
        return 0
    elif a <= 2:
        return 1
    elif a <= 4:
        return 2
    elif a <= 6:
        return 3
    else:
        return 4

for line in fileinput.input():
    s = line.split(" | ")
    r = sum(1 for ix, i in enumerate(s[0]) if i != s[1][ix])
    print(m[prio(r)])
