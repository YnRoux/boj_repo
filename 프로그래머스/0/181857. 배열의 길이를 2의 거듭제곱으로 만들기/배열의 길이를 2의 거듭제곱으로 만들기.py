def solution(arr):
    n = len(arr)
    if n & (n-1) == 0:
        return arr
    target = 1
    while target < n:
        target *= 2
    return arr + [0] * (target - n)