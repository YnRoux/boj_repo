def solution(a, d, included):
    isum = 0
    asum = a
    for i in range(len(included)):
        if included[i]:
            isum += i
            asum += a
    return asum - a + d * isum