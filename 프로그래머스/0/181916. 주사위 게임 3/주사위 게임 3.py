def solution(a, b, c, d):
    l1 = [a, b, c, d]
    l2 = list(set(l1)) 
    if len(l2) == 1:
        return 1111 * l2[0]
    if len(l2) == 2:
        cnt = l1.count(l2[0])
        if cnt == 1:
            return (10 * l2[1] + l2[0])**2
        elif cnt == 2:
            return (l2[0] + l2[1]) * abs(l2[0] - l2[1])
        elif cnt == 3:
            return (10 * l2[0] + l2[1]) ** 2
    if len(l2) == 3:
        for i in range(3):
            if l1.count(l2[i]) == 2:
                idx = i
        l2.pop(idx)
        return l2[0] * l2[1]
    if len(l2) == 4:
        return min(l1)