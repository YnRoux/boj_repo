def solution(arr):
    l = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            l[i][j] = arr[j][i]
    return int(l==arr)