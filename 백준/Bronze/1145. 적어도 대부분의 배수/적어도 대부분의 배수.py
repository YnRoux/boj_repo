l = list(map(int, input().split()))
m = min(l)
while 1:
    cnt = 0
    for e in l:
        if m % e == 0:
            cnt += 1
    if cnt > 2:
        break
    m += 1
print(m)