def solution(str_list, ex):
    res = ""
    for s in str_list:
        if not ex in s:
            res += s
    return res