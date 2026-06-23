def solution(my_string, queries):
    ls = list(my_string)
    for query in queries:
        a, b = query[0], query[1]
        temp = ls[a:b+1]
        temp = temp[::-1]
        ls = ls[:a] + temp + ls[b+1:]
    out_str = "".join(ls)
    return out_str