for i in range(0,int(input())):
    s1 = input()
    s2 = input()
    str=''
    for j in range(0,len(s1)):
        if s1[j]==s2[j]:
            str+='.'
        else:
            str+='*'
    print(s1)
    print(s2)
    print(str+'\n')
