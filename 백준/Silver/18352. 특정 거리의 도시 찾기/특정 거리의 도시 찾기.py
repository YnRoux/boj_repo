import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m, k, x = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    distance = [-1] * (n + 1)
    distance[x] = 0
    
    queue = deque([x])
    
    while queue:
        now = queue.popleft()
        
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                queue.append(next_node)
    
    found = False
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)
            found = True
            
    if not found:
        print(-1)

if __name__ == "__main__":
    solve()