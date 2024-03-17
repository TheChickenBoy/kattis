n = int (input())
d = input()
a = input()

if n%2==0:
    e = True
else:
    e = False
for i, b in enumerate(d):
    if e:
        if b == a[i]:
            continue
        else:
            print("Deletion failed")
            exit()
    else:
        if b == a[i]:
            print("Deletion failed")
            exit()
        else:
            continue
print("Deletion succeeded")