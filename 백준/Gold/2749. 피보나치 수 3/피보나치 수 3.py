def solve():
    n = int(input())
    m = n % 1500000

    fibo = [0] * (m+2)
    fibo[1] = 1
    for i in range(2, m+1):
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000
    
    print(fibo[m])

if __name__ == "__main__":
    solve()