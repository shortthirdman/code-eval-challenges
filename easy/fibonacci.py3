import fileinput

def fibonacci(a):
    if a < 2:
        return a
    b, c = 0, 1
    for _ in range(a-1):
        b, c = c, b + c
    return c

for line in fileinput.input():
    print(fibonacci(int(line)))
