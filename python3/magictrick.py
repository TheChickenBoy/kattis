s = input()
t = ''.join(set(s))
if len(s) == len(t):
    print(1)
else:
    print(0)