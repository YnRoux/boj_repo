from collections import deque

def solution(maps):
    # n: 행의 개수, m: 열의 개수
    n = len(maps)
    m = len(maps[0])
    
    # 상, 하, 좌, 우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS를 위한 큐 생성 및 시작점 추가
    queue = deque()
    queue.append((0, 0))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 목적지에 도착했으면 거리 반환
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 1. 맵 범위를 벗어나지 않고
            # 2. 벽(0)이 아니며
            # 3. 처음 방문하는 길(1)인 경우 (이미 방문했으면 숫자가 1보다 큼)
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 이전 위치의 값에 +1을 하여 거리를 기록 (방문 처리 겸용)
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    # 큐를 다 비웠는데도 목적지에 도달 못했으면 -1 반환
    return -1