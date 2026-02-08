def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())
    
    count = 0
    for i in range(n):
        count += 1
        
        rem = a[i] - b

        if rem > 0:
            count += (rem // c)
            if rem % c > 0:
                count += 1
    print(count)

if __name__ == "__main__":
    solve()