def mp(a, b, c):
    if b == 1: return a % c
    else:
        d = mp(a, b//2, c)
        if b % 2 == 0: return (d**2) % c
        else: return (d**2 * a) % c

a, b, c = map(int, input().split())
print(mp(a, b, c))