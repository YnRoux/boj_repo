def solution(intStrs, k, s, l):
    ret = []
    for i in intStrs:
        if int(i[s:s+l]) > k:
            ret.append(int(i[s:s+l]))
    return ret