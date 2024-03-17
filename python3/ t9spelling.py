två = ['a','b','c']
tre = ['d','e','f']
fyra = ['g','h','i']
fem = ['j','k','l']
sex = ['m','n','o']
sju = ['p','q','r','s']
åtta = ['t','u','v']
nio = ['w','x','y','z']
for i in range(int(input())):
    l = input()
    o = ""
    pressed = None
    for c in l:
        if c in två:
            if pressed == 2:
                o += ' '
            pressed = 2
            o += '2'*(två.index(c)+1)
        elif c in tre:
            if pressed == 3:
                o += ' '
            pressed = 3
            o += '3'*(tre.index(c)+1)
        elif c in fyra:
            if pressed == 4:
                o += ' '
            pressed = 4
            o += '4'*(fyra.index(c)+1)
        elif c in fem:
            if pressed == 5:
                o += ' '
            pressed = 5
            o += '5'*(fem.index(c)+1)
        elif c in sex:
            if pressed == 6:
                o += ' '
            pressed = 6
            o += '6'*(sex.index(c)+1)
        elif c in sju:
            if pressed == 7:
                o += ' '
            pressed = 7
            o += '7'*(sju.index(c)+1)
        elif c in åtta:
            if pressed == 8:
                o += ' '
            pressed = 8
            o += '8'*(åtta.index(c)+1)
        elif c in nio:
            if pressed == 9:
                o += ' '
            pressed = 9
            o += '9'*(nio.index(c)+1)
        else:
            if pressed == 0:
                o += ' 0'
            else:
                o += '0'
            pressed = 0

    print(f"Case #{i+1}: {o}")