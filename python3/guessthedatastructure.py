from sys import stdin

for l in stdin:
    ops = []
    vals = []
    s = True
    q = True
    pq = True
    imp = False
    """
    Läs av input
    om 1: lägg till i en lista(?)
    om 2: ta bort ur listan och ändra booleaner
    """
    for i in range(int(l)):
        op, v = map(int,input().split())
        if op == 1:
            vals.append(v)
        else:
            if not v:
                imp = True
            elif v == vals[0]:
                s = False
                if max(vals) != v:
                    pq = False
            else:
                q = False
                if max(vals) != v:
                    pq = False
            try:
                vals.remove(v)
            except ValueError:
                imp = True
        #ops.append(v)
    if imp:
        print("impossible")
    elif s and (q or pq):
        print("not sure")
    elif q  and (s or pq):
        print("not sure")
    elif s and (not q and not pq):
        print("stack")
    elif q and (not s and not pq):
        print("queue")
    elif pq and (not q and not s):
        print("priority queue")
    else:
        print("impossible")
    