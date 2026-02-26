import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
v = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
count = 0

def dfs(now):
    global count
    visited[now] = True

    for next_node in graph[now]:
        if not visited[next_node]:
            count += 1
            dfs(next_node)

dfs(1)
print(count)