while True:
    l = list(map(float,input().split()))
    if len(l)== 1:
        exit()

    print(
        (abs(l[0]-l[2])**l[4] + abs(l[1]-l[3])**l[4])**(1/l[4])
    )
    