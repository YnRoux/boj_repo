import sys
input = sys.stdin.readline
n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color, visited, current_grid):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and current_grid[nx][ny] == color:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

def get_area_count(current_grid):
    visited = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, current_grid[i][j], visited, current_grid)
                count += 1
    return count

normal_count = get_area_count(grid)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

blind_count = get_area_count(grid)

print(f"{normal_count} {blind_count}")