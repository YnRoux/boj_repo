def solution(num_list):
    e, o = 0, 0
    for i in range(0,len(num_list),2):
        o += num_list[i]
    for i in range(1,len(num_list),2):
        e += num_list[i]
    return max(e,o)
        