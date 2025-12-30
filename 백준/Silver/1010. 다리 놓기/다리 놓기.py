def fact(n):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p

def bi(n, k):
    no = fact(n)
    de = fact(n-k) * fact(k)
    return no // de

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(bi(b, a))