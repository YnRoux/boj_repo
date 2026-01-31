s = int(input())
n, res = 0, 0
for i in range(1, s+1):
    n += i
    res += 1
    if n > s:
        res -= 1
        break
print(res)