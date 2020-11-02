from textwrap import wrap
l = input()

a = wrap(l,int(len(l)/3))

if a[0] == a[1]:
    print(a[0])
elif a[1]==a[2]:
    print(a[1])
else:
    print(a[2])