num = list(map(int, input().split()))
print(max(num[1]-num[0],num[2]-num[1])-1)