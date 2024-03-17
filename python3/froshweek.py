def mergeSortInversions(lst):
    l = len(lst)
    if l == 1:
        return lst, 0
    else:
        m = l//2
        a = lst[:m]
        b = lst[m:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = j = 0
        inv = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inv += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c,inv

lst = [int(input()) for _ in range(int(input()))]
print(mergeSortInversions(lst)[1])

 