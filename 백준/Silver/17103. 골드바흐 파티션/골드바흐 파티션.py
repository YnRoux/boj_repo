import sys
input = sys.stdin.readline
prime = [1] * 1000001

for i in range(2, 1000001):
    if prime[i] == 1:
        for j in range(2*i, 1000001, i):
            prime[j] = 0

t = int(input().strip())

for _ in range(t):
    cnt = 0
    n = int(input().strip())
    for p in range(2, n // 2 + 1):
        if prime[p] and prime[n - p]:
            cnt += 1
    print(cnt)
        