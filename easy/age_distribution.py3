import collections, fileinput

cat = collections.OrderedDict(
     ((0, "This program is for humans"),
      (3, "Still in Mama's arms"),
      (5, "Preschool Maniac"),
     (12, "Elementary school"),
     (15, "Middle school"),
     (19, "High school"),
     (23, "College"),
     (66, "Working for the man"),
    (101, "The Golden Years")))

for line in fileinput.input():
    r, s = cat[0], int(line)
    for k in cat:
        if s < k:
            r = cat[k]
            break
    print(r)
