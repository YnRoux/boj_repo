import sys
def solve():
    t = sys.stdin.readline().strip()
    t = int(t)
    if t % 10 != 0:
        print("-1")
        return
    a = t // 300
    t %= 300
    b = t // 60
    t %= 60
    c = t // 10
    t %= 10
    print(f"{a} {b} {c}")
solve()