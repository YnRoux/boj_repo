# 17608
import sys
input = sys.stdin.readline
n = int(input().strip())
bars = [int(input().strip()) for _ in range(n)]
proj = bars[-1]
cnt = 1
for i in range(n):
    comp = bars[-1-i]
    if comp > proj:
        proj = comp
        cnt += 1
print(cnt)