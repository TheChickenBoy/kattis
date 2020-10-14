l = list(input())
s = ""
count = 0
for c in reversed(l):
    if c == '<':
        count+=1
        #l[i] = '\0'
    elif count > 0:
        count-=1
        #l[i] = '\0'
    else:
        s = c + s    
print(s)
# for c in l:
#     if c != '\0':
#         s+=c
# print(s)
