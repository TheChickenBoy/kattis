l1 = input()
l2 = input()

c1 = l1.count('S')
c2 = l2.count('S')

n = c1*c2
if n == 0:
    print('0')
    exit()
a = ['S(']*(n)
a.append('0)')
b = [')']*(n-1)
a.extend(b)
print(*a,sep='')