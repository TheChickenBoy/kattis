from sys import stdin,stdout
g,t,n = map(int, stdin.readline().split())
weights = list(map(int, stdin.readline().split()))
stdout.write(str(int(((g-t)*.9)-sum(weights))))