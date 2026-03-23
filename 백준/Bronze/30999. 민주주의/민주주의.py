def solve():
    n, m = map(int, input().split())
    cnt = 0
    for _ in range(n):
        x = input().count("X")
        if x < m // 2 + 1:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    solve()