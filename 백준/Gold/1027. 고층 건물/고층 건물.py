def solve():
    n = int(input())
    h = list(map(int, input().split()))
    res = [0] * n
    
    for i in range(n-1):
        temp = -1e9
        for j in range(i+1, n):
          if temp  < (h[j] - h[i]) / (j - i):
              res[i] += 1
              res[j] += 1
              temp = (h[j] - h[i]) / (j - i)
    
    print(max(res))

if __name__ == "__main__":
    solve()