import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
grid = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque([(x, y)])
    grid[x][y] = 0
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count

result = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for r in result:
    print(r)