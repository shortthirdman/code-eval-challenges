import fileinput

def happy(a):
    r = 0
    while (a > 0):
        b = a % 10
        r += b*b
        a //= 10
    return r

for line in fileinput.input():
    a = int(line)
    b = [a]
    for i in range(127):
        if a <= 1:
            break
        a = happy(a)
        if a in b:
            a = 0
            break
    print(1 if a == 1 else 0)
