m, n = map(int, input().split())
for i in range(m, n+1):
    if i == 1: continue
    if i == 2: print(2)
    if i % 2 == 0: continue
    for j in range(3, int(i**(1/2))+1, 2):
        if i % j == 0: break
    else: print(i)