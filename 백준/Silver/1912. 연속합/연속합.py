def solve():
    n = int(input())
    l = list(map(int, input().split()))

    current_sum = max_sum = l[0]

    for i in range(1, n):
        current_sum = max(l[i], current_sum + l[i])

        if current_sum > max_sum:
            max_sum = current_sum

    print(max_sum)

if __name__ == "__main__":
    solve()