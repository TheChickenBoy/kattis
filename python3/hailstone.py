from sys import stdin
n = int(stdin.readline().strip())

nums = [n]

while True:
    if n == 1:
        print(sum(nums))
        exit()
    elif n%2 == 0:
        n//=2
        nums.append(n)
    else:
        n=(3*n)+1
        nums.append(n)