import sys
def foo(a):
    count = 0
    while a:
        count+=1
        i = 1
        for i in range(1,len(a)):
            if a[i-1]>a[i]:
                break
            elif i == len(a)-1:
                i += 1
        a = a[i:]
    return count

l = list(map(int,sys.stdin.readlines()[1:]))
print(foo(l))