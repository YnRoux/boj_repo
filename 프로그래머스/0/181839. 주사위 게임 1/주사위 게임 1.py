def solution(a, b):
    if a & b & 1 == 1:
        return a**2 + b**2
    elif (a&1==1) | (b&1==1):
        return 2 * (a + b)
    else:
        return abs(a - b)