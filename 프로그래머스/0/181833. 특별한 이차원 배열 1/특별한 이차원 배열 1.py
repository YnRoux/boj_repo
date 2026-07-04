def solution(n):
    l = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        l[i][i] = 1
    return l