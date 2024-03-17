from math import log10
from sys import stdin

def is_repeating(numr, denr):
    mp = {}
    rem = numr % denr
    while ((rem != 0) and (rem not in mp) and len(mp)<100):
        mp[rem] = True
        rem = rem * 10
        rem = rem % denr
    
    if (rem == 0):
        return False
    else:
        return True

for l in stdin:
    t,a,b = map(int,l.split())

    if is_repeating((t**a-1),(t**b-1)):
        print(f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits.")
    else:
        try:
            num = (t**a-1)//(t**b-1)
            if int(log10(num))+1 > 100:
                print(f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits.")
            else:
                print(f"({t}^{a}-1)/({t}^{b}-1)",num)
        except:
            print(f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits.")

