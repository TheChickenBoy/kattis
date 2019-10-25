s = input()

w = lc = uc = sym = 0
for c in s:
    if c == '_':
        w+=1
    elif c.islower():
        lc += 1
    elif c.isupper():
        uc += 1
    else:
        sym+=1
print("%.15f" % (w/len(s)))
print("%.15f" % (lc/len(s)))
print("%.15f" % (uc/len(s)))
print("%.15f" % (sym/len(s)))
