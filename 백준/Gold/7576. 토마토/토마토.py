from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:

                graph[nx][ny] = graph[x][y] + 1

                queue.append((nx, ny))

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()

res = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit()

        res = max(res, graph[i][j])

print(res - 1)