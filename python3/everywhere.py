for i in range(0,int(input())):
    dict={}
    for j in range(0,int(input())):
        t = input()
        if t in dict:
            dict[t]+=1
        else:
            dict[t]=1
    print(len(dict))
