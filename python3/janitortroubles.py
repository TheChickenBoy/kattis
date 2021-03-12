from math import cos,sqrt,pi
s1,s2,s3,s4 = map(int,input().split())
# Bretschneider′s formula
s = (s1+s2+s3+s4)/2
print(sqrt((s-s1)*(s-s2)*(s-s3)*(s-s4)-((s1*s2*s3*s4)*(cos(pi/2)**2))))