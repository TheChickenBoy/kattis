from sys import stdin
d = {}
translate = False

for l in stdin:
    if l == '\n': 
        translate = True
        continue
    if not translate:
        word = l.split()
        d[word[1]] = word[0]
    else:
        try:
            print(d[l[:-1]])
        except KeyError:
            print("eh")