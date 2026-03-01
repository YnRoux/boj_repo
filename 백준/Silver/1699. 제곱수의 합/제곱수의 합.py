def solve():
    n = int(input())
    INF = int(1e9)
    dp = [0] + [INF] * n

    for i in range(1, n+1):
        for j in range(1, int(i**0.5)+1):
            dp[i] = min(dp[i], dp[i - j**2] + 1)

    print(dp[-1])

if __name__ == "__main__":
    solve()