def solution(my_string, m, c):
    s = ""
    for i in range(0, len(my_string), m):
        try:
            s += my_string[i+c-1]
        except:
            pass
    return s