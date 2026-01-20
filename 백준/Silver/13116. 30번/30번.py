import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    while 1:
        if a == b:
            print(10 * a)
            break
        if a > b:
            a //= 2
        else:
            b //= 2