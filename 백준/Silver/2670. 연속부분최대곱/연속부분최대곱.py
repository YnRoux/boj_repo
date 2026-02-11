import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    l = [float(input().rstrip()) for _ in range(n)]


    dp = [0] * n
    dp[0] = l[0]

    for i in range(1, n):
        dp[i] = max(l[i], dp[i-1] * l[i])

    print(f"{max(dp):.3f}")

if __name__ == "__main__":
    solve()