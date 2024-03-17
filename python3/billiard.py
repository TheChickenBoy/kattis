from math import degrees, atan

def main():
    a, b, s, m, n = map(int, input().split())
    if a == b == s == m == n == 0:
        exit()
    
    angle = degrees(atan((b * n) / (a * m)))
    dist = ((b * n) ** 2 + (a * m) ** 2) ** 0.5
    veloc = dist / s
    print("{:.2f} {:.2f}".format(angle, veloc))
    
    main()

if __name__ == '__main__':
    main()