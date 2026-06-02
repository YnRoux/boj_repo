def solution(quiz):
    res = []
    for prob in quiz:
        LHS, RHS = prob.split('=')[0], prob.split('=')[1]
        if eval(LHS) == int(RHS):
            res.append('O')
        else:
            res.append('X')
    return res