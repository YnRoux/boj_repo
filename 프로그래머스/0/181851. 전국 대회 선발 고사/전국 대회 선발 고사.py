def solution(rank, attendance):
    available = []
    for i in range(len(rank)):
        if attendance[i]:
            available.append((rank[i], i))
    available.sort()
    a = available[0][1]
    b = available[1][1]
    c = available[2][1]
    return 10000 * a + 100 * b + c