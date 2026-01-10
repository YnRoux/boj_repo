import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
l, s = [0], 0
for i in range(n):
    s += nums[i]
    l.append(s)
for _ in range(m):
    a, b = map(int, input().split())
    print(l[b] - l[a-1])