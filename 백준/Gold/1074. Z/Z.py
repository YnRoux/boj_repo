import sys

def solve():
    n, r, c = map(int, sys.stdin.readline().split())
    answer = 0
    while n != 0:
        n -= 1
        half = 2 ** n
        
        if r < half and c < half:
            answer += 0
            
        elif r < half and c >= half:
            answer += half * half
            c -= half
            
        elif r >= half and c < half:
            answer += 2 * (half * half)
            r -= half
            
        else:
            answer += 3 * (half * half)
            r -= half
            c -= half
            
    print(answer)

solve()