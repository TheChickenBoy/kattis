for _ in range(int(input())):
    d = {}
    for _ in range(int(input())):
        art, num = input().split()
        if art in d:
            d[art] += int(num)
        else:
            d[art] = int(num)
    ds = sorted(d, key=lambda x: (-d[x], x))
    print(len(ds))
    for key in ds:
        print(key, d[key])
