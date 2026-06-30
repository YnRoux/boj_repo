def solution(my_strings, parts):
    res = ""
    for string, (s, e) in zip(my_strings, parts):
        res += string[s:e+1]
    return res