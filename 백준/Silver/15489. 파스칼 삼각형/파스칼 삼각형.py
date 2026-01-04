def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def comb(a, b):
    return fact(a) // (fact(b) * fact(a-b))

def pas_tri(r):
    return [[comb(n, c) for c in range(n+1)] for n in range(r)]


r, c, w = map(int, input().split())
r -= 1
c -= 1
l = pas_tri(r+w)
s = 0
for i in range(w):
    for j in range(i+1):
        s += l[r+i][c+j]
print(s)