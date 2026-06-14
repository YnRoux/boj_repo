def solution(arr):
    n = max(len(arr), len(arr[0]))
    for i in range(len(arr)):
        arr[i] += [0] * (n - len(arr[i]))
    while len(arr) < n:
        arr.append([0] * n)
    return arr