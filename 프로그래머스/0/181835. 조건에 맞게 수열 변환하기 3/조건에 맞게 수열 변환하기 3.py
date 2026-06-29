def solution(arr, k):
    return list(map(lambda x: x * k if k & 1 != 0 else x + k, arr))