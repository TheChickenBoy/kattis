l = input()
s=''
i=0
while i < len(l):
    if l[i] not in ('a', 'e', 'i', 'o', 'u'):
        s+=l[i]
        i+=1
    else:
        s+=l[i]
        i+=3
print(s)
