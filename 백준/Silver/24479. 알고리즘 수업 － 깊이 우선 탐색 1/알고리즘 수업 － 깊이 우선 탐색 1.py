import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(curr):
    global count
    visited[curr] = count

    for next_node in graph[curr]:
        if visited[next_node] == 0:
            count += 1
            dfs(next_node)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
count = 1

dfs(r)

for i in range(1, n+1):
    print(visited[i])