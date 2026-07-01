def solution(my_string, indices):
    res = ""
    for i in range(len(my_string)):
        if not i in indices:
            res += my_string[i]
    return res