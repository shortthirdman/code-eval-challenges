import fileinput, re

for line in fileinput.input():
    print(min([len(i) for i in re.findall("X\.*Y", line)]) - 2)
