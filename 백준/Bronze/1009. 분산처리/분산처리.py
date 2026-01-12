import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    a, b = map(int, input().strip().split())
    p = pow(a, b, 10)
    
    if p == 0:
        print(10)
    else:
        print(p)