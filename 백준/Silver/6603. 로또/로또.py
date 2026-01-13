def lotto(idx, depth):
    if depth == 6:
        print(*res)
    else:
        for i in range(idx, k):
            res.append(l[i])
            lotto(i+1, depth+1)
            res.pop()

import sys
input = sys.stdin.readline

while 1:
    in_str = input().strip()
    if in_str == "0":
        break
    l = list(map(int, in_str.split()))
    k = l.pop(0)
    res = []
    lotto(0, 0)
    print()
