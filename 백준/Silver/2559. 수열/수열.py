def solve():
    n, k = map(int, input().split())
    temps = list(map(int, input().split()))

    current_sum = sum(temps[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum += temps[i]
        current_sum -= temps[i-k]

        if current_sum > max_sum:
            max_sum = current_sum

    print(max_sum)
    

if __name__ == "__main__":
    solve()