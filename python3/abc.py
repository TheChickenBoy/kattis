num = input()
num = num.split()
for i in range(0,3):
    num[i] = int(num[i])
num = sorted(num)
let = input()

st = ''
for i in range(0,3):
    if let[i] == 'A':
        st+=str(num[0])+' '
    elif let[i] == 'B':
        st+=str(num[1])+' '
    else:
        st+=str(num[2])+' '
print(st)
