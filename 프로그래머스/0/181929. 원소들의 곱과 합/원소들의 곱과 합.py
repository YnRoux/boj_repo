def solution(num_list):
    sum_square = sum(num_list)**2
    prod = 1
    for i in num_list:
        prod *= i
    return int(prod < sum_square)