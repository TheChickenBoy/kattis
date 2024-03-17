m = int(input())
f = int(input())
d = int(input())

print( "Monnei" if min(m,f,d) == m else "Fjee" if min(m,f,d) == f else "Dolladollabilljoll")

# print("Monnei" if (m := int(input())) == min(m, f := int(input()), d := int(input())) else "Fjee" if f == min(m, f, d) else "Dolladollabilljoll")
