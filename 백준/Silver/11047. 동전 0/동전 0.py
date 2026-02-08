import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    count = 0

    for i in range(n-1, -1, -1):
        if k == 0:
            break
        count += k // coins[i]
        k %= coins[i]
    print(count)

if __name__ == "__main__":
    solve()