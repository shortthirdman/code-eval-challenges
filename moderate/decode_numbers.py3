import fileinput

def decode(s):
    s = s.lstrip('03456789')
    if len(s) < 2:
        return 1
    if s[1] == '0' or (s[0] == '2' and s[1] in '789'):
        return decode(s[2:])
    return 2 if len(s) == 2 else decode(s[1:]) + decode(s[2:])

for line in fileinput.input():
    print(decode(line.rstrip('\n')))
