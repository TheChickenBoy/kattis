from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

def build_output(index_li,words,idx):
    print(words[idx], end='')
    for i in index_li[idx]:
        build_output(index_li, words, i)

n = int(stdin.readline())
words = ['']*n
index_li = [[] for _ in range(n)]

for i in range(n):
    words[i] = stdin.readline().strip()

idx1 = 0
idx2 = 0
for i in range(n - 1):
    idx1, idx2 = map(int,stdin.readline().split())
    index_li[idx1-1].append(idx2-1)

build_output(index_li,words,idx1-1)
print()