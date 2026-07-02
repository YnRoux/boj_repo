def solution(numbers, n):
    s = 0
    for num in numbers:
        if s > n:
            return s
        s += num
    return s