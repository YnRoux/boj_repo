import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    for _ in range(n):
        a, b = map(int, input().rstrip().split())
        print(a+b, a*b)

t = int(input().rstrip())
for _ in range(t):
    solve()
    