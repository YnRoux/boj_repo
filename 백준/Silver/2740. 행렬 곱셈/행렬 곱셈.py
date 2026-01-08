import sys
input = sys.stdin.readline

def transpose(mat):
    return [list(row) for row in zip(*mat)]

def inner_product(v1, v2):
    return sum([ai * bi for ai, bi in zip(v1, v2)])

def mat_prod(a, b):
    b_transpose = transpose(b)
    res = []
    
    n_len = len(a)
    k_len = len(b[0])
    
    for i in range(n_len):
        l = []
        for j in range(k_len):
            l.append(inner_product(a[i], b_transpose[j]))
        res.append(l)
    return res


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

final_matrix = mat_prod(a, b)

for row in final_matrix:
    print(*row)