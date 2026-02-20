import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def solve():
    n, m, k, x = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append((v, 1))
    distance = [INF] * (n + 1)
    
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    found = False
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)
            found = True
            
    if not found:
        print(-1)

if __name__ == "__main__":
    solve()