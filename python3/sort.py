import sys

input = []
out = {}
for l in sys.stdin:
    last_in = l
input_str = last_in.split()

for w in input_str:
    if w in out:
        out[w] += 1
    else:
        out[w] = 1

sort_w = sorted(out, key=out.get, reverse=True)

str = ""
for w in sort_w:
    for i in range(0,out[w]):
        str = str + w + " "
print(str)
#print(sort_w)
