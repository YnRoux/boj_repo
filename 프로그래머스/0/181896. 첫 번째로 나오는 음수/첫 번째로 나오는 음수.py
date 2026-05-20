def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            break
    else:
        i = -1
    return i