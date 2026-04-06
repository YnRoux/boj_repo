import sys
from collections import deque
import copy
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []
for r in range(n):
    for c in range(m):
        if grid[r][c] == 0:
            empty.append((r, c))
        elif grid[r][c] == 2:
            virus.append((r, c))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_safe_zone(temp_grid):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp_grid[nx][ny] == 0:
                    temp_grid[nx][ny] = 2
                    queue.append((nx, ny))
    
    count = 0
    for row in temp_grid:
        count += row.count(0)
    return count

max_safe = 0

for walls in combinations(empty, 3):
    temp_grid = copy.deepcopy(grid)
    
    for r, c in walls:
        temp_grid[r][c] = 1
    
    max_safe = max(max_safe, get_safe_zone(temp_grid))

print(max_safe)