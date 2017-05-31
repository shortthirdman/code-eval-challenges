import fileinput

moy = {i: ix for ix, i in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}

def month(s):
    return 12 * (int(s[4:]) - 1990) + moy[s[:3]]

for line in fileinput.input():
    w = set()
    for i in line.split("; "):
        t0, t1 = [month(j) for j in i.split('-')]
        w |= set(range(t0, t1+1))
    print(len(w)//12)
