def solution(str1, str2):
    s = ''
    for c1, c2 in zip(str1, str2):
        s += c1 + c2
    return s