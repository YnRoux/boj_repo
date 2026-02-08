import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    pwdict = {}
    for _ in range(n):
        site, password = input().rstrip().split()
        pwdict[site] = password
    for _ in range(m):
        check = input().rstrip()
        print(pwdict[check])

if __name__ == "__main__":
    solve()