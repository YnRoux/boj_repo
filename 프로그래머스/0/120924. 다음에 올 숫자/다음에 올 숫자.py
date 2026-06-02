def det(l):
    if l[0] + l[2] == 2 * l[1]:
        return 'ari'
    elif l[0] * l[2] == l[1]**2:
        return 'geo'
    
def solution(common):
    if det(common) == 'ari':
        d = common[1] - common[0]
        ans = common[-1] + d
    elif det(common) == 'geo':
        r = common[1] // common[0]
        ans = common[-1] * r
    return ans