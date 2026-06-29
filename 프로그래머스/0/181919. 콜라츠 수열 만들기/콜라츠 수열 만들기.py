def solution(n):
    l = [n]
    while n != 1:
        if n & 1 == 0:
            n //= 2
        else:
            n = 3*n + 1
        l.append(n)
    return l
            