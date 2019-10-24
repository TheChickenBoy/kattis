import sys
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']

for l in sys.stdin:
    l = l.split()
    x = int(l[0])
    if x == 0:
        exit()
    s=''
    for c in l[1]:
        i = letters.index(c)
        i += x
        if i >= len(letters):
            i -= len(letters)
        s+=letters[i]
    print(s[::-1])
