n = int(input())
l = list(map(int, input().split()))

start, end = 0, n-1

res = abs(l[start] + l[end])
res_start = start
res_end = end

while start < end:
    tmp = l[start] + l[end]
    
    if abs(tmp) < res:
        res = abs(tmp)
        res_start = start
        res_end = end

        if res == 0:
            break
    
    if tmp < 0:
        start += 1
    else:
        end -= 1

print(l[res_start], l[res_end])
