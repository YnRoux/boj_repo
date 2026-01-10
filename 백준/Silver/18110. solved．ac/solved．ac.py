def round_off(n):
    if (n - int(n)) >= 0.5:
        return int(n) + 1
    else:
        return int(n)
    
import sys
input = sys.stdin.readline

n = int(input().strip())
if n == 0:
    print(0)
else:
    l = [int(input().strip()) for _ in range(n)]
    l.sort()
    boundary = round_off(n * 0.15)
    print(round_off(sum(l[boundary : n - boundary])/(n-2*boundary)))
