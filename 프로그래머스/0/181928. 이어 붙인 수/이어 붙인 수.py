def solution(num_list):
    odd = ''
    even = ''
    for n in num_list:
        if n & 1 == 0:
            even += str(n)
        else:
            odd += str(n)
    return int(odd) + int(even)