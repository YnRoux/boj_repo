n = int(input())
l = ['*' * i for i in range(1, n+1)]
for i in range(n):
    print(l[i])
for i in range(n-2, -1, -1):
    print(l[i])