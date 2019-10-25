w = input().split()
if w[0][-1] == 'e':
    print(w[0]+'x'+w[1])
elif w[0][-1] in ["a","i","o","u"]:
    print(w[0][:len(w[0])-1]+'ex'+w[1])
elif w[0][-1] == 'x' and w[0][-2] == 'e':
    print(w[0]+w[1])
else:
    print(w[0]+'ex'+w[1])
