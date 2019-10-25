import datetime
n = list(map(int,input().split()))
d = datetime.datetime(2009, n[1],n[0]).weekday()
if d == 0:
    print("Monday")
elif d == 1:
    print("Tuesday")
elif d == 2:
    print("Wednesday")
elif d == 3:
    print("Thursday")
elif d == 4:
    print("Friday")
elif d == 5:
    print("Saturday")
else:
    print("Sunday")
