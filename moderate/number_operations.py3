import fileinput, itertools

for line in fileinput.input():
    a, f = [int(i) for i in line.split()], False
    for i in itertools.permutations(a):
        for o1 in range(3):
            if o1 == 0:
                r1 = i[0] + i[1]
            elif o1 == 1:
                r1 = i[0] - i[1]
            else:
                r1 = i[0] * i[1]
            for o2 in range(3):
                if o2 == 0:
                    r2 = r1 + i[2]
                elif o2 == 1:
                    r2 = r1 - i[2]
                else:
                    r2 = r1 * i[2]
                for o3 in range(3):
                    if o3 == 0:
                        r3 = r2 + i[3]
                    elif o3 == 1:
                        r3 = r2 - i[3]
                    else:
                        r3 = r2 * i[3]
                    for o4 in range(3):
                        if o4 == 0:
                            r4 = r3 + i[4]
                        elif o4 == 1:
                            r4 = r3 - i[4]
                        else:
                            r4 = r3 * i[4]
                        if r4 == 42:
                            f = True
                            break
                    if f:
                        break
                if f:
                    break
            if f:
                break
        if f:
            break
    print("YES" if f else "NO")
