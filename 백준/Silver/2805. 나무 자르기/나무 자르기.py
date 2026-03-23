def solve():
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))

    start = 0
    end = max(heights)
    
    while start <= end:
        mid = (start + end) // 2
        total = sum(h - mid for h in heights if h > mid)

        if total >= m:
            res = mid 
            start = mid + 1
        else:
            end = mid - 1
            
    print(res)

if __name__ == "__main__":
    solve()