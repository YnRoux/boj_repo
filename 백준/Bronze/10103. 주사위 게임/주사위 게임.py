import sys
def solve():
    n_str = sys.stdin.readline().strip()
    n = int(n_str)
    chang_score = 100
    sang_score = 100
    for _ in range(n):
        c, s = map(int, sys.stdin.readline().split())
        if c > s:
            sang_score -= c
        elif s > c:
            chang_score -= s  
    print(chang_score)
    print(sang_score)
solve()