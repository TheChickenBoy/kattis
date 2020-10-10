l = input()
s = ""
indexs = []
index = 0
for i, c in enumerate(l):
    if c != '<':
        #s+=c
        #index += 1
        indexs.append(i)
    #else:
    #    if index > 0:
    #        index -= 1
        #index.append[i]
o=""
for i in indexs:
    o+=l[i]
    #if c == "<":
    #    s = s[:-1]
    #else:
    #    s+=c
print(o)
#print(s[0:index])