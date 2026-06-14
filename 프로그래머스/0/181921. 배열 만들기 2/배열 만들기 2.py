def solution(l, r):
    ls = []
    for i in range(l, r+1):
        s = str(i)
        det = 1
        for c in s:
            if c not in "50":
                det = 0
                break
        if det == 1:
            ls.append(i)
    if ls:
        return ls
    else:
        return [-1]