import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    idx = 1
    for _ in range(n):
        r = int(input_data[idx])
        e = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        profit_with_ad = e - c
        if profit_with_ad > r:
            print("advertise")
        elif profit_with_ad == r:
            print("does not matter")
        else:
            print("do not advertise")
solve()