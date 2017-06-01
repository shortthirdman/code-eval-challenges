"""find the longest repeated substring in a given text"""
import fileinput

for line in (i.rstrip('\n') for i in fileinput.input()):
    l = len(line)
    if not l:
        print("NONE")
        continue
    m = ''
    n = 1
    start = 0
    while n <= (l - start) / 2:
        f = False
        for i in range(start, l - n):
            subst = line[i : i + n]
            if not subst.strip():
                continue
            if subst in line[i + n : l]:
                m = subst
                start = i
                f = True
                n += 1
                break
        if not f:
            break
    print("NONE" if m == '' else m)
