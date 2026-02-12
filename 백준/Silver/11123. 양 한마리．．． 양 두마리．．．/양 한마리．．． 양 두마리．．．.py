import sys
from collections import deque

input = sys.stdin.readline

def solve():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    h, w = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#" and not visited[i][j]:
                count += 1
                queue = deque([(i, j)])
                visited[i][j] = True

                while queue:
                    x, y = queue.popleft()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < h and 0 <= ny < w:
                            if grid[nx][ny] == "#" and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
    print(count)

t = int(input())

for _ in range(t):
    solve()