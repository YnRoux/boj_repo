def solution(num_list):
    num_list.sort()
    for _ in range(5):
        num_list.pop(0)
    return num_list