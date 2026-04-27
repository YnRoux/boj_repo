import sys

input = sys.stdin.read

def solve():
    data = input().split()
    sabun_to_busan_rail = int(data[0])
    busan_to_sabun_flight = int(data[1])
    
    if sabun_to_busan_rail <= busan_to_sabun_flight:
        print("high speed rail")
    else:
        print("flight")

solve()