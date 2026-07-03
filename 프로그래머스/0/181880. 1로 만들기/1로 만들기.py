def solution(num_list):
    def oper(n):
        i = 0
        while n != 1:
            if n & 1 == 0: n //= 2
            else: n = (n-1) // 2
            i += 1
        return i
    j = 0
    for n in num_list:
        j += oper(n)
    return j
                