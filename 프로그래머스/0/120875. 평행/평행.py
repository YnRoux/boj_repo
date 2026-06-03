def solution(dots):
    p1, p2, p3, p4 = dots
    
    def is_parallel(a, b, c, d):
        dy1, dx1 = b[1] - a[1], b[0] - a[0]
        dy2, dx2 = d[1] - c[1], d[0] - c[0]
        return dy1 * dx2 == dy2 * dx1
    if is_parallel(p1, p2, p3, p4) or is_parallel(p1, p3, p2, p4) or is_parallel(p1, p4, p2, p3):
        return 1
    return 0