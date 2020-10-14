from sys import stdin
from math import pi

for l in stdin:
    dv = list(map(int, l.split()))
    if dv[0] == 0:
        exit()
    v_tot = pi*((dv[0]/2)**2)*dv[0]
    v_left = v_tot - dv[1]
    cone = pi*((dv[0]/2)**2)*(dv[0]/3)
    tilt = v_left - cone
    s_cy = tilt*1.5
    s_r = (s_cy/(2*pi))**(1. /3)
    
    print("{:.9f}".format(s_r*2))

    