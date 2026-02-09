import sys
input = sys.stdin.readline

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        price_list = list(map(int, input().split()))
        profit = 0
        max_val = 0

        for i in range(n-1, -1, -1):
            if price_list[i] > max_val:
                max_val = price_list[i]
            else:
                profit += max_val - price_list[i]

        print(profit)
                
if __name__ == "__main__":
    solve()