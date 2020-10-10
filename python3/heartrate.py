for i in range(int(input())):
    l = list(map(float,(input().split())))
    print("{:.4f} {:.4f} {:.4f}".format((((l[0]-1)*60)/l[1]),(((l[0])*60)/l[1]),(((l[0]+1)*60)/l[1])))