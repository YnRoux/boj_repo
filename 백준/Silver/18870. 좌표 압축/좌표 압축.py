import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
ls = sorted(list(set(l)))
rk_map = {val: idx for idx, val in enumerate(ls)}
res = []
for e in l:
    res.append(str(rk_map[e]))
print(' '.join(res))