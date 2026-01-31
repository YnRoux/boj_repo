n = int(input())
a, b = 1, 0
for _ in range(n-1):
    a, b = a + b, a
print(a)