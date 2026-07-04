def solution(strArr):
    l = []
    for s in strArr:
        l.append(len(s))
    ls = [l.count(x) for x in list(set(l))]
    return max(ls)