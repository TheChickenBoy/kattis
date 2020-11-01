from sys import stdin
d = {
    'B' : '1',
    'F' : '1',
    'P' : '1',
    'V' : '1',
    'C' : '2',
    'G' : '2',
    'J' : '2',
    'K' : '2',
    'Q' : '2',
    'S' : '2',
    'X' : '2',
    'Z' : '2',
    'D' : '3',
    'T' : '3',
    'L' : '4',
    'M' : '5',
    'N' : '5',
    'R' : '6',
    'A' : '',
    'E' : '',
    'I' : '',
    'O' : '',
    'U' : '',
    'H' : '',
    'W' : '',
    'Y' : '',
}

for l in stdin:
    s = ''
    last = ''
    for c in l:
        if c in d:
            if d[c] == last:
                continue
            s += d[c]
            last = d[c]
    print(s)