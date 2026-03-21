import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0

def solve(x, y, k):
    global white, blue
    color = paper[x][y]

    for i in range(x, x + k):
        for j in range(y, y + k):
            if paper[i][j] != color:
                new_k = k // 2
                solve(x, y, new_k)
                solve(x, y + new_k, new_k)
                solve(x + new_k, y, new_k)
                solve(x + new_k, y + new_k, new_k)
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1

solve(0, 0, n)

print(white)
print(blue)