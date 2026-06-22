def solution(a, b, c):
    l = [a, b, c]
    if len(set(l)) == 3:
        return a + b + c
    elif len(set(l)) == 2:
        return (a+b+c) * (a**2 + b**2 + c**2)
    elif len(set(l)) == 1:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)