import fileinput

for line in filter(lambda x: x != '\n', fileinput.input()):
    st = line.split(",")
    print(st[0].rfind(st[1][0]))
