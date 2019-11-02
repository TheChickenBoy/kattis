for i in range(int(input())):
    abc = "abcdefghijklmnopqrstuvwxyz"
    l = input()
    for c in l:
        if c.lower() in abc:
            abc = abc.replace(c.lower(),'')
    print('pangram') if len(abc) == 0 else print('missing ' + abc)
