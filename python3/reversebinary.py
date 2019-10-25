l = []
def decimalToBinary(n):
    if(n > 1):
        decimalToBinary(n//2)
    l.append(n%2)

def binaryToDecimal(b):
    decimal, i, n = 0, 0, 0
    while(b != 0):
        dec = b % 10
        decimal = decimal + dec * pow(2, i)
        b = b//10
        i += 1
    print(decimal)

decimalToBinary(int(input()))
l.reverse()
s=''
for c in l:
    s+=str(c)
binaryToDecimal(int(s))
