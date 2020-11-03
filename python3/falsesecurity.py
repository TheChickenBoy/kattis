from sys import stdin
d = {
    'A' : (2,'.-'),
    'B' : (4,'-...'),
    'C' : (4,'-.-.'),
    'D' : (3,'-..'),
    'E' : (1,'.'),
    'F' : (4,'..-.'),
    'G' : (3,'--.'),
    'H' : (4,'....'),
    'I' : (2,'..'),
    'J' : (4,'.---'),
    'K' : (3,'-.-'),
    'L' : (4,'.-..'),
    'M' : (2,'--'),
    'N' : (2,'-.'),
    'O' : (3,'---'),
    'P' : (4,'.--.'),
    'Q' : (4,'--.-'),
    'R' : (3,'.-.'),
    'S' : (3,'...'),
    'T' : (1,'-'),
    'U' : (3,'..-'),
    'V' : (4,'...-'),
    'W' : (3,'.--'),
    'X' : (4,'-..-'),
    'Y' : (4,'-.--'),
    'Z' : (4,'--..'),
    '_' : (4,'..--'),
    '.' : (4,'---.'),
    ',' : (4,'.-.-'),
    '?' : (4,'----')
}

d2 = {
    '.-'   : 'A',
    '-...' : 'B',
    '-.-.' : 'C',
    '-..'  : 'D',
    '.'    : 'E',
    '..-.' : 'F',
    '--.'  : 'G',
    '....' : 'H',
    '..'   : 'I',
    '.---' : 'J',
    '-.-'  : 'K',
    '.-..' : 'L',
    '--'   : 'M',
    '-.'   : 'N',
    '---'  : 'O',
    '.--.' : 'P',
    '--.-' : 'Q',
    '.-.'  : 'R',
    '...'  : 'S',
    '-'    : 'T',
    '..-'  : 'U',
    '...-' : 'V',
    '.--'  : 'W',
    '-..-' : 'X',
    '-.--' : 'Y',
    '--..' : 'Z',
    '..--' : '_',
    '---.' : '.',
    '.-.-' : ',',
    '----' : '?',
}

for l in stdin:
    ns = ''
    s = []
    o = ''
    for c in l:
        if c == '\n':
            break
        t = d[c]
        s.append(t[0])
        ns += t[1]
    i = 0

    s = reversed(s)
    for n in s:
        letter = ns[:n]
        ns = ns[n:]
        o+=d2[letter]
    # while ns:
    #     letter = d2[ns[:s[i]]]
    #     i+=1
    #     ns = ns[s[i]:]
    #     o += letter
    #s = reversed(s)
    print(o)