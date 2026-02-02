n, k = map(int, input().split())

numerator = 1
denominator = 1
for i in range(n, n-k, -1):
    numerator *= i
for i in range(1, k+1):
    denominator *= i
res = (numerator // denominator) % 10007
print(res)