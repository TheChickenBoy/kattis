from sys import stdin, stdout
n = int(stdin.readline())
stdout.write(str((n//2 + 1)**2+(n//2 + 1)) if n%2==1 else str((n//2 + 1)**2))

