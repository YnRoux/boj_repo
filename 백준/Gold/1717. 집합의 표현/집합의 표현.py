import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve():
    n, m = map(int, input().split())

    parent = [i for i in range(n+1)]

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    
    def union_parent(a, b):
        root_a = find_parent(a)
        root_b = find_parent(b)
        if root_a != root_b:
            parent[root_a] = root_b

    for _ in range(m):
        op, a, b = map(int, input().split())

        if op == 0:
            union_parent(a, b)
        else:
            if find_parent(a) == find_parent(b):
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    solve()