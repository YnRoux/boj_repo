import sys
input = sys.stdin.readline

def solve():
    global i
    i += 1
    a, b, c = map(int, input().rstrip().split())
    
    if sum([a,b,c]) <= 2 * max([a,b,c]):
        print(f"Case #{i}: invalid!")
    elif a == b == c:
        print(f"Case #{i}: equilateral")
    elif (a == b) or (b == c) or (c == a):
        print(f"Case #{i}: isosceles")
    else:
        print(f"Case #{i}: scalene")

t = int(input().rstrip())
for i in range(t):
    solve()