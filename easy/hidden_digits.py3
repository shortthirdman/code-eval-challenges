import fileinput

def clean(a):
    if a in "abcdefghij":
        return chr(ord(a) - 49)
    return a

for line in fileinput.input():
    st = ''.join(clean(c) for c in line if c in "0123456789abcdefghij")
    print("NONE" if len(st) == 0 else st)
