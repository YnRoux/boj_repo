def solution(n):
    if n & 1 == 0:
        idx = n//2
        return 4*((idx*(idx+1)*(2*idx+1))//6)
    else:
        idx = (n-1)//2
        return ((1+idx)*(n+1))//2