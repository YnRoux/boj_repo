n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a, b = sorted(a), sorted(b, reverse=True)
s = 0
for ai, bi in zip(a, b):
    s += ai * bi
print(s)