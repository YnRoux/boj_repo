def solution(arr, queries):
    l = []
    for s, e, k in queries:
        filtered = list(filter(lambda x: x > k, arr[s:e+1]))
        l.append(min(filtered) if filtered else -1)
    return l