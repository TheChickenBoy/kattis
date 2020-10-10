l = input()
#s=[]
s = ""
t = 0
for i, c in enumerate(l):
    if c == "<":
        l[i] = "\0"
        t+=1 
    elif t>0:
        l[i] = '\0'
        t-=1
        #s.append(c)
        #s+=c
o=''
for i in len(l):
    if l[i]!='\0':
        o+=l[i]     
print(o)