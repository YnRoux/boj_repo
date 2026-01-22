import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))

    graph[y][x] = 0

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((nx, ny))


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    cnt = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(j, i)
                cnt += 1 
    print(cnt)