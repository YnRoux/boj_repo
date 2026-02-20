import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a != root_b:
        parent[root_a] = root_b
        return True
    return False

def solve():
    n, m = map(int, input().split())
    
    parent = list(range(n + 1))
    operations = 0
    
    for _ in range(m):
        u, v = map(int, input().split())
        if not union(parent, u, v):
            operations += 1
            
    num_groups = 0
    for i in range(1, n + 1):
        if parent[i] == i:
            num_groups += 1
            
    operations += (num_groups - 1)
    
    print(operations)

if __name__ == "__main__":
    solve()