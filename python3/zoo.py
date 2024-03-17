from sys import stdin, stdout

line = stdin.readline()
i=0
while line:
    i+=1
    if int(line) == 0:
        exit()
    d = {}
    for _ in range(int(line)):
        l = stdin.readline().strip()
        l = l.lower()
        t = l.split()
        if len(t) > 1:
            t[0] = t[-1]
        if t[0] in d:
            d[t[0]] += 1
        else:
            d[t[0]] = 1
    sorted_dict = dict(sorted(d.items()))
    print(f"List {i}:")
    for k in sorted_dict.keys():
        print(k,"|",sorted_dict[k])
    line = stdin.readline()