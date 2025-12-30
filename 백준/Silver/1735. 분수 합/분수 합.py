def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())
n = n1*d2 + n2*d1
d = d1*d2
gd = gcd(n, d)
print(f"{n // gd} {d // gd}")