def solution(picture, k):
    res = []
    for row in picture:
        r = ""
        for i in row:
            r += i * k
        for _ in range(k):
            res.append(r)
    return res