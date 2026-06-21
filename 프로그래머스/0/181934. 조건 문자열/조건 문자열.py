def solution(ineq, eq, n, m):
    if eq == "=":
        if ineq == "<":
            a = int(n <= m)
        elif ineq == ">":
            a = int(n >= m)
    if eq == "!":
        if ineq == "<":
            a = int(n < m)
        elif ineq == ">":
            a = int(n > m)
    return a
            