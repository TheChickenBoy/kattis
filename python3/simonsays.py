for i in range(int(input())):
    l = input()
    if "Simon says" in l:
        print(l[len("Simon says")+1:])
