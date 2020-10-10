n,m = input().split()
n=int(n)
m=int(m)
s=""
if (m-n)<0:
    s = "s" if (((m-n)*-1) != 1) else s
    print(f"Dr. Chaz needs {(m-n)*-1} more piece"+s+" of chicken!")
else:
    s = "s" if ((m-n) != 1) else s
    print(f"Dr. Chaz will have {(m-n)} piece"+s+" of chicken left over!")