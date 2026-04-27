import sys

def solve():
    line = sys.stdin.readline().split()
    if not line:
        return
    a, i = map(int, line)
    print(a * (i - 1) + 1)

solve()