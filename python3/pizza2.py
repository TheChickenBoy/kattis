from math import pi
x,y = map(int,input().split())
print(100*(1-(((pi*x**2) -(pi*(x-y)**2))/(pi*x**2))))
