n = int(input())
tl = list(map(int, input().split()))
t, p = map(int, input().split())
s = 0
for e in tl:
    if e == 0:
       pass
    else:
        s += (e-1) // t + 1
print(s)
print(f"{n//p} {n%p}")