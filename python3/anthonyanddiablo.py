from math import pi, sqrt
from sys import stdin, stdout
a,n = map(float,stdin.readline().split())
stdout.write('Diablo is Happy!\n' if 2 * pi * sqrt(a/pi) <= n else 'Need more materials!\n')