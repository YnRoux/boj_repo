import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

N = int(input())
M = int(input())

parent = [i for i in range(N + 1)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            union(parent, i + 1, j + 1)

plan = list(map(int, input().split()))

root = find(parent, plan[0])
possible = True

for i in range(1, M):
    if find(parent, plan[i]) != root:
        possible = False
        break

print("YES" if possible else "NO")