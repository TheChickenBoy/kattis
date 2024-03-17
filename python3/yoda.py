n = list(input())
m = list(input())

if len(n) > len(m):
    d = len(n) - len(m)
    a = ['0']*d
    m = a+m
elif len(n) < len(m):
    d = len(m) - len(n)
    a = ['0']*d
    n = a+n

h = max(len(n),len(m))
n_out = []
m_out = []
for i in range(h):
    if n[i]>m[i]:
        n_out.append(n[i])
    elif m[i]>n[i]:
        m_out.append(m[i])
    elif m[i] == n[i]:
        n_out.append(m[i])
        m_out.append(m[i])

print(int("".join(n_out)) if len(n_out)>0 else "YODA")
print(int("".join(m_out)) if len(m_out)>0 else "YODA")
