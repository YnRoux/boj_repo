import sys

input = sys.stdin.readline

def solve():
    try:
        line1 = input().split()
        if not line1:
            return
        n, m = map(int, line1)
    except ValueError:
        return

    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    dp = [[0] * m for _ in range(n)]

    dp[0][0] = grid[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    for i in range(n):
        print(dp[i][m-1], end=' ')
    print()

solve()