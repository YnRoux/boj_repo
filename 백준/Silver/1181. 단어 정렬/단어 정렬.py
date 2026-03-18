import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    d = input().strip()
    l.append(d)
ul = list(set(l))
ls = sorted(ul, key=lambda x: (len(x), x))
for e in ls:
    print(e)