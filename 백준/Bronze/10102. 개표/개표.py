import sys

def solve():
    v = int(sys.stdin.readline())
    votes = sys.stdin.readline().strip()
    
    count_a = votes.count('A')
    count_b = votes.count('B')
    
    if count_a > count_b:
        print('A')
    elif count_b > count_a:
        print('B')
    else:
        print('Tie')

solve()