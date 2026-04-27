import sys
def solve():
    input = sys.stdin.read().split()    
    n = int(input[0])
    max_prize = 0
    current = 1
    for _ in range(n):
        dice = sorted(list(map(int, input[current:current+3])))
        current += 3
        a, b, c = dice
        if a == b == c:
            prize = 10000 + a * 1000
        elif a == b or b == c:
            prize = 1000 + b * 100
        else:
            prize = c * 100
        if prize > max_prize:
            max_prize = prize
    print(max_prize)
solve()