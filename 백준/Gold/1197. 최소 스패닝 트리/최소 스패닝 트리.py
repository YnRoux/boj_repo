import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())

parent = [i for i in range(V+1)]

edges = []
result = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

for edge in edges:
    w, u, v = edge
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += w

print(result)