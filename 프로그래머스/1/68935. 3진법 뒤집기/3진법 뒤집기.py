def solution(n):
    import math
    m = 3
    idx_max = int(math.log(n)/math.log(3))
    digits = []
    for i in range(idx_max, -1, -1):
        digits.append(n//3**i)
        n %= 3 ** i
    digits.reverse()
    val = sum([digits[i] * 3 ** (idx_max - i) for i in range(idx_max +1)])
    return val