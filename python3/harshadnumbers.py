n = input()
num = int(n)

def sum_of_str(num_str):
    s = 0
    for c in num_str:
        s+=int(c)
    return s

while(True):
    s = sum_of_str(str(num))
    if num%s == 0:
        print(num)
        exit()
    num+=1