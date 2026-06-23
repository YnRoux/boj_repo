def solution(numLog):
    operation = {1:'w', -1:'s', 10:'d', -10:'a'}
    s = ''
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        s += operation[diff]
    return s