while True:
    s = ['?']*32
    x = int(input())
    if x == 0:
        exit()
    for q in range(x):
        inst = input().split()
        if inst[0] == "CLEAR":
            s[int(inst[1])] = '0'
        elif inst[0] == "SET":
            s[int(inst[1])] = '1'  
        elif inst[0] == "OR":
            i = s[int(inst[1])]
            j = s[int(inst[2])]
            if i == '1' or j == '1':
                s[int(inst[1])] ='1'
            elif i == '0' and j == '0':
                s[int(inst[1])] ='0'
            elif i == '?' or j == '?':
                s[int(inst[1])] ='?'
        elif inst[0] == "AND":
            i = s[int(inst[1])]
            j = s[int(inst[2])]
            if i == '1' and j == '1':
                s[int(inst[1])] ='1'
            elif i == '0' or j == '0':
                s[int(inst[1])] ='0'
            elif i == '?' or j == '?':
                s[int(inst[1])] ='?'
    print(*reversed(s), sep='')

    