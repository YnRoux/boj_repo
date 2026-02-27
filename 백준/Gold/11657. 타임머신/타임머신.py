import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    edges = []
    
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    INF = float('inf')
    dist = [INF] * (n+1)
    dist[1] = 0

    negative_cycle = False

    for i in range(n):
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

                if i == n-1:
                    negative_cycle = True

    if negative_cycle:
        print(-1)
    else:
        for i in range(2, n+1):
            if dist[i] == INF:
                print(-1)
            else:
                print(dist[i])

if __name__ == "__main__":
    solve()