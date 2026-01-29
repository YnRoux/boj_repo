n = int(input())
l = list(map(int, input().split()))
s = 0
l.sort(reverse=True)
for i in range(n):
    s += sum(l[i:])
print(s)