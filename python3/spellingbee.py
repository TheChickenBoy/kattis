from sys import stdin, stdout
import re
letters = list(stdin.readline().strip())
for _ in range(int(stdin.readline())):
    l = stdin.readline().strip()
    if letters[0] not in l or len(l)<4 or re.findall(f"[^{''.join(letters)}]", l):
        continue
    stdout.write(l+"\n")