def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
rings = list(map(int,input().split()))
first = rings[0]
for i in range(1,n):
    g = gcd(first, rings[i])
    print(f"{first//g}/{rings[i]//g}")